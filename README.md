# PodBump
Script for bumping podspec versions

No argument increments the patch 


```
podbump
"1.0.1" -> "1.0.2"
```

Pass as argument `minor`, `major` or `patch` to increment the respective version component:


```
podbump minor
"1.0.2" -> "1.1.0"
```

```
podbump major
"1.2.3" -> "2.0.0"
```

The script prints the new version for use in other build scripts
