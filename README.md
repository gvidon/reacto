Reacto is a set of CLI commands to maintain react.js apps and components based on [specific structure](#component-structure). It is mostly a wrapper around https://github.com/audreyr/cookiecutter with some additional features like adding additional parts (like actions or routes) into existing component.

The main reason why it is not an npm, but pypi package is that there is no cookiecutter port for node.js with non-CLI API.

## Component structure
*To be edited*

## Installation
Simply install pypi package:
```shell
pip install reacto
```

CLI script will deploy into some of your `bin/` directories, make sure it is listed in `$PATH`.

## Available commands and options

### `start_app`
*Not yet available*

### `start_component [options] <component path>`
Start new component. You can pass absolute/relative path or just compoentn name, in which case component will be created in current directory.

#### `--actions`
If passed `<component path>/actions.js` file created.

#### `--no-flow`
*To be edited*

#### `--reducers`
If passed `<component path>/reducers.js` file created.

#### `--routes`
If passed `<component path>/routes.js` file created.
