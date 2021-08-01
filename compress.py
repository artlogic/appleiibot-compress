import importlib
import sys
from unidecode import unidecode

modules = (
    "x000",
    "x001",
    "x002",
    "x003",
    "x004",
    "x005",
    "x006",
    "x007",
    "x009",
    "x00a",
    "x00b",
    "x00c",
    "x00d",
    "x00e",
    "x00f",
    "x010",
    "x011",
    "x012",
    "x013",
    "x014",
    "x015",
    "x016",
    "x017",
    "x018",
    "x01d",
    "x01e",
    "x01f",
    "x020",
    "x021",
    "x022",
    "x023",
    "x024",
    "x025",
    "x026",
    "x027",
    "x028",
    "x029",
    "x02a",
    "x02c",
    "x02e",
    "x02f",
    "x030",
    "x031",
    "x032",
    "x033",
    "x04d",
    "x04e",
    "x04f",
    "x050",
    "x051",
    "x052",
    "x053",
    "x054",
    "x055",
    "x056",
    "x057",
    "x058",
    "x059",
    "x05a",
    "x05b",
    "x05c",
    "x05d",
    "x05e",
    "x05f",
    "x060",
    "x061",
    "x062",
    "x063",
    "x064",
    "x065",
    "x066",
    "x067",
    "x068",
    "x069",
    "x06a",
    "x06b",
    "x06c",
    "x06d",
    "x06e",
    "x06f",
    "x070",
    "x071",
    "x072",
    "x073",
    "x074",
    "x075",
    "x076",
    "x077",
    "x078",
    "x079",
    "x07a",
    "x07b",
    "x07c",
    "x07d",
    "x07e",
    "x07f",
    "x080",
    "x081",
    "x082",
    "x083",
    "x084",
    "x085",
    "x086",
    "x087",
    "x088",
    "x089",
    "x08a",
    "x08b",
    "x08c",
    "x08d",
    "x08e",
    "x08f",
    "x090",
    "x091",
    "x092",
    "x093",
    "x094",
    "x095",
    "x096",
    "x097",
    "x098",
    "x099",
    "x09a",
    "x09b",
    "x09c",
    "x09d",
    "x09e",
    "x09f",
    "x0a0",
    "x0a1",
    "x0a2",
    "x0a3",
    "x0a4",
    "x0ac",
    "x0ad",
    "x0ae",
    "x0af",
    "x0b0",
    "x0b1",
    "x0b2",
    "x0b3",
    "x0b4",
    "x0b5",
    "x0b6",
    "x0b7",
    "x0b8",
    "x0b9",
    "x0ba",
    "x0bb",
    "x0bc",
    "x0bd",
    "x0be",
    "x0bf",
    "x0c0",
    "x0c1",
    "x0c2",
    "x0c3",
    "x0c4",
    "x0c5",
    "x0c6",
    "x0c7",
    "x0c8",
    "x0c9",
    "x0ca",
    "x0cb",
    "x0cc",
    "x0cd",
    "x0ce",
    "x0cf",
    "x0d0",
    "x0d1",
    "x0d2",
    "x0d3",
    "x0d4",
    "x0d5",
    "x0d6",
    "x0d7",
    "x0f9",
    "x0fa",
    "x0fb",
    "x0fc",
    "x0fd",
    "x0fe",
    "x0ff",
    "x1d4",
    "x1d5",
    "x1d6",
    "x1d7",
    "x1f1",
    "x1f6",
)

map = {}

for m in modules:
    data = importlib.import_module(f"unidecode.{m}").data
    for i, d in enumerate(data):
        ordinal = int(f"0{m}{hex(i)[2:].zfill(2)}", 16)
        weight = 2
        # deal with twitter character weights
        if (
            0 <= ordinal <= 4351
            or 8192 <= ordinal <= 8205
            or 8208 <= ordinal <= 8223
            or 8242 <= ordinal <= 8247
        ):
            weight = 1
        if d and len(d) > weight:
            map[d] = chr(ordinal)

done = set()
shortest = ""


def compress(work, keys):
    global shortest

    for key in keys:
        next_work = work.replace(key, map[key])
        if len(next_work) < len(shortest):
            shortest = next_work
        if next_work not in done:
            done.add(next_work)
            next_keys = keys[:]
            next_keys.remove(key)
            compress(next_work, next_keys)


if __name__ == "__main__":
    fn = ''.join(sys.argv[1:])
    with open(fn) as f:
        orig = f.read()

    keys = []
    for k in map.keys():
        if k in orig:
            keys.append(k)

    shortest = orig
    compress(orig, keys)

    if orig == unidecode(shortest):
        print("Original length:", len(orig))
        print("Compressed length:", len(shortest))
        print()
        print(shortest)
    else:
        print("Compression error!")
        sys.exit(1)
