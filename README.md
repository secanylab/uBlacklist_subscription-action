# uBlacklist Subscription

[![update-uBlacklist-subscription](https://github.com/secanylab/uBlacklist_subscription/actions/workflows/update.yaml/badge.svg)](https://github.com/secanylab/uBlacklist_subscription/actions/workflows/update.yaml)

uBlacklist Subscription List

## How to customize metadata

```
// content farm meta
data/content-farm_raw.txt
data/content-farm_match_patterns_raw.txt

// ml translation meta
data/ml-translation_raw.txt
data/ml-translation_match_patterns_raw.txt
```

:balloon: *If your browser has configured the [subscription rules](https://github.com/secanylab/uBlacklist_subscription#for-subscription-providers), and after modifying the metadata, the github action will automatically update the subscription list.*


## Filter Toolkit

```
  src/filter_content_farm.py      // gen content farm list.
  src/filter_ml_translation.py    // gen ml translation list.
```

## For subscription providers

```
# Raw
https://raw.githubusercontent.com/secanylab/uBlacklist_subscription/master/content-farm_v1.txt
https://raw.githubusercontent.com/secanylab/uBlacklist_subscription/master/ml-translation_v1.txt

# CDN
https://cdn.jsdelivr.net/gh/secanylab/uBlacklist_subscription@master/content-farm_v1.txt
https://cdn.jsdelivr.net/gh/secanylab/uBlacklist_subscription@master/ml-translation_v1.txt
```

## License

uBlacklist Subscription is licensed under [MIT License](LICENSE.txt).
