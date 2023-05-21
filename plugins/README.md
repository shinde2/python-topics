# Plugins

## Running the example

- Create virtual env
-
  ```
  pip install -e core_pkg 
  pip install -e plugin_mul
  pip install -e plugin_div
  ```
- Run the core app for addition
  ```
  run-app add 10 2
  ```
- Load the plugin for multiplication
  ```
  run-app mul 10 2
  ```
- Run the plugin for division
  ```
  run-app div 10 2
  ```


### Resources
```
https://setuptools.pypa.io/en/latest/userguide/entry_point.html
```