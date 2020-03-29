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

Add the script to your path to be able to call it from any directory. 



The script prints the new version for use in other build scripts. Example:

```
# increments podspec version, create a tag with the new version, commit the change and push the changes and the tag.
git tag "$(podbump)";git add YOUR_POD_NAME.podspec;git commit -m"version bump";git push;git push --tags
```

If travis is set up to deploy the pod, an alias for the above command will allow you to tag and deploy with one command.
