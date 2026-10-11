#!/usr/bin/env python3
"""从 cs2-slim 注册表生成生成器静态数据 data.js。

数据源（单一事实源）:
  - registry/features.json  -> FEATURES（platform / depends=requires）
  - registry/maps.json       -> MAPS

用法:
  python generate_data.py [--registry-dir ../cs2-slim-repo/registry] [--output data.js]

生成的 data.js 被 index.html 引用，避免生成器硬编码与注册表不同步。
"""
import argparse
import json
import os

# 展示顺序（不在列表中的功能自动排到末尾；功能集合以注册表为准）
FEATURE_ORDER = [
    "bots", "metamod", "metamod-win", "css", "css-win",
    "swiftly", "swiftly-win", "plugify", "plugify-win",
    "modsharp", "modsharp-win", "link-manager",
]


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry-dir", default=os.path.join(os.path.dirname(__file__), "..", "cs2-slim-repo", "registry"),
                    help="cs2-slim-repo/registry 目录路径")
    ap.add_argument("--output", default=os.path.join(os.path.dirname(__file__), "data.js"),
                    help="输出 data.js 路径")
    args = ap.parse_args()

    feats = load_json(os.path.join(args.registry_dir, "features.json"))["features"]
    maps = load_json(os.path.join(args.registry_dir, "maps.json"))["maps"]

    features_js = {}
    for name, meta in feats.items():
        features_js[name] = {
            "platform": meta.get("platform", "both"),
            "depends": list(meta.get("requires") or []),
        }

    order = [f for f in FEATURE_ORDER if f in feats] + [f for f in feats if f not in FEATURE_ORDER]

    lines = [
        "/* 自动生成：由 generate_data.py 从 registry/features.json + maps.json 生成，请勿手改。 */",
        "window.GENERATOR_DATA = {",
        "  MAPS: " + json.dumps(list(maps.keys()), ensure_ascii=False, indent=2).replace("\n", "\n  "),
        "  ,",
        "  FEATURES: " + json.dumps(features_js, ensure_ascii=False, indent=2).replace("\n", "\n  "),
        "  ,",
        "  FEATURE_ORDER: " + json.dumps(order, ensure_ascii=False),
        "};",
        "",
    ]
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print(f"已生成 {args.output}")
    print("  MAPS:", ", ".join(maps))
    print("  FEATURES:", ", ".join(feats))
    print("  FEATURE_ORDER:", ", ".join(order))


if __name__ == "__main__":
    main()