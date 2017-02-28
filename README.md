Reacto is a set of CLI commands to maintain react.js apps and components based on [specific structure](#component-structure) we use in ottofeller.com. It is mostly a wrapper around https://github.com/audreyr/cookiecutter with some additional features like adding extra parts (like actions or routes) into existing component.

The main reason why it is not an npm, but pypi package is that there is no cookiecutter port for node.js with non-CLI API.

## Component structure
Reacto declares app structure which is aimed to be easily scalable, with infinitely deep hierarchy of nested components.

Rules:
* each component must be named with camel case, like `SomeNestedComponent`
* each component structure is **the same**
* non-components dirs must be named in lower case, using `-` as words separator.

According to declared rules component dir includes following parts.

### assets/
CSS/images/fonts — all related assets are placed there.

### SomeNestedComponent/
Nested component dir name starts with capital letter.

### index.js
Entry point of any component. Should export all of its parts and describe presentational view:
* HTML structure of component
* CSS imports
* other assets import.

View should be described/connected to redux in this file and **exported as default value**. This file should always be presented in each component.

Other parts of component should be exported with name:
* `routes` — routes related to the component
* `reducers`
* `actions`

Parts of a component must be imported separately to make imports less heavy, not importing entire object including all its parts:

```javascript
import {reducers as financialReducers} from 'Financial';
```

### routes.js
Routing to nested components, based on `react-router` library.

```javascript
// app/SomeComponent/routes.js
import React from 'react';
import {IndexRoute, Route} from 'react-router';
import DetailsView from 'Entity/Details';
import ListView from 'Entity/List';

export default () => <Route path='contacts'>
	<IndexRoute component={ListView}/>
	<Route path='details/:id' component={DetailsView} />
</Route>
```

### actions.js
Redux actions should be described as functions here. Also this file should include actions types constants.

```javascript
export const actionsTypes {
  ADD_ENTITY,
  REMOVE_ENTITY
};

export const addEntity = payload => ({
  type     : module.exports.actionsTypes.ADD_ENTITY,
  firstName: payload.firstName,
  lastName : payload.lastName
});
```

### reducers.js
Reducers functions according to redux.

```javascript
function entity(state, action) {
  ({
    ADD_ENTITY: () => {id: 1, firstName: action.firstName, lastName: action.lastName}
  }[state] || () => state)()
}

function entities(state, action) {
  return ({
    ADD_ENTITY: () => [
      ...state,
      contact(undefined, action)
    ],

    REMOVE_ENTITY: () => _.reject(state, (C) => C.id === action.id)
  }[state] || () => state)()
}

export default entities
```

## Installation
Simply install pypi package:
```shell
pip install reacto
```

CLI script will deploy into some of your `bin/` directories, make sure it is listed in `$PATH`.

## Usage
Example, create compoentn `NewComponent` in the current dir:

```shell
reacto start-component --no-flow NewComponent
```

## Available commands and options

### `start-app [options] <app path>`
*Not yet available*

### `start-component [options] <component path>`
Start new component. You can pass absolute/relative path or just compoentn name, in which case component will be created in current directory.

#### `--actions`
If passed `<component path>/actions.js` file created.

#### `--no-flow`
Disable [FlowType](https://flowtype.org/) — do not apply its annotations.

#### `--reducers`
If passed `<component path>/reducers.js` file created.

#### `--routes`
If passed React Router 4 will be applied to `idex.js`.

#### `--route-path`
Path specified on root component of routes tree, which is `routes.js:<Route />`.
