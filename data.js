/* 自动生成：由 generate_data.py 从 registry/features.json + maps.json 生成，请勿手改。 */
window.GENERATOR_DATA = {
  MAPS: [
    "de_dust2",
    "de_mirage",
    "de_inferno",
    "de_ancient",
    "de_anubis",
    "de_cache",
    "de_nuke",
    "de_overpass",
    "de_train",
    "de_vertigo"
  ]
  ,
  FEATURES: {
    "bots": {
      "platform": "both",
      "depends": []
    },
    "metamod": {
      "platform": "linux",
      "depends": []
    },
    "metamod-win": {
      "platform": "windows",
      "depends": []
    },
    "css": {
      "platform": "linux",
      "depends": [
        "metamod"
      ]
    },
    "css-win": {
      "platform": "windows",
      "depends": [
        "metamod-win"
      ]
    },
    "link-manager": {
      "platform": "both",
      "depends": []
    },
    "swiftly": {
      "platform": "linux",
      "depends": []
    },
    "swiftly-win": {
      "platform": "windows",
      "depends": []
    },
    "plugify": {
      "platform": "linux",
      "depends": [
        "metamod"
      ]
    },
    "plugify-win": {
      "platform": "windows",
      "depends": [
        "metamod-win"
      ]
    },
    "modsharp": {
      "platform": "linux",
      "depends": []
    },
    "modsharp-win": {
      "platform": "windows",
      "depends": []
    }
  }
  ,
  FEATURE_ORDER: ["bots", "metamod", "metamod-win", "css", "css-win", "swiftly", "swiftly-win", "plugify", "plugify-win", "modsharp", "modsharp-win", "link-manager"]
};
