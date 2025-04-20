---
title: Authoring an Extension
---

# Authoring Griffin Analytics Studio Extensions

This guide will walk you through the process of creating Griffin Analytics Studio extensions and deploying them in your Griffin Analytics Studio-based application. Please make sure to be aware of how to create a Griffin Analytics Studio based application and the different available extension mechanisms of Griffin Analytics Studio (Plugins vs. Extensions) before you continue reading.

As an example, we are going to add a menu item _Say hello_ that displays a notification "Hello world!". This article guides you through the necessary steps.

## Prerequisites

Prerequisites information is available from the Griffin Analytics Studio repository.

## Project Layout

Please refer to the guide to create Griffin Analytics Studio applications to get familiar with the default project layout and generate a Griffin Analytics Studio project with the example 'hello world' extension using our Yeoman Generator.

## A Custom Griffin Analytics Studio Extension

Let's look at the generated code for our extension in the `hello-world` folder. Let’s start with the `package.json`. It specifies the package’s metadata, its dependencies to the Griffin Analytics Studio core package, a few scripts and dev dependencies, and the extension itself. Please note that the following listing might be outdated, please always refer to the generated examples from our Yeoman Generator.

The keyword `griffin-analytics-studio-extension` is important: It allows a Griffin Analytics Studio app to identify and install Griffin Analytics Studio extensions from `npm`.

```json
{
  "name": "hello-world",
  "keywords": [
    "griffin-analytics-studio-extension"
  ],
  "version": "0.0.0",
  "files": [
    "lib",
    "src"
  ],
  "dependencies": {
    "@theia/core": "latest" 
  },
  "devDependencies": {
    "rimraf": "latest",
    "typescript": "~5.4.5"
  },
  "scripts": {
    "prepare": "yarn run clean && yarn run build",
    "clean": "rimraf lib",
    "build": "tsc",
    "watch": "tsc -w"
  },
  "theiaExtensions": [
    {
      "frontend": "lib/browser/hello-world-frontend-module"
    }
  ]
}
```
*(Note: Dependency `@theia/core` might need updating later to reflect Griffin-specific core packages if they exist)*

As you can see, the extension is a dedicated package that just depends on Griffin Analytics Studio. However, as the extension contributes features to our application, it needs to be wired at runtime. To achieve this in a modular way, in Griffin Analytics Studio, everything is wired up via dependency injection. An extension defines one or more dependency injection modules. This is where it binds its contribution implementations to the respective contribution interface. The modules are listed in the `package.json` of the extension package. An extension can contribute to the frontend, e.g. providing a UI extension, as well as to the backend, e.g. contributing a language server. When the application starts, the union of all these modules is used to configure a single, global dependency injection container on each, the frontend and the backend. The runtime will then collect all contributions of a specific kind by means of a multi-inject.

The last property `theiaExtensions` in the `package.json` above is where we list the JavaScript modules that export the DI modules defining the contribution bindings of our extension. In our case, we only provide a frontend capability (a command and a menu entry). Analogously, you could also define contributions to the backend, e.g. a language contribution with a language server.

Griffin Analytics Studio defines a plethora of contribution interfaces that allow extensions to add their behaviour to various aspects of the application. Browse the documentation section 'Platform Concepts & APIs' or search for interfaces with the name `*Contribution` to get an idea. An extension implements the contribution interfaces belonging to the functionality it wants to deliver. In this example, we are going to implement a `CommandContribution` and a `MenuContribution`. Other ways for extensions to interact with a Griffin Analytics Studio application are via one of the various _services_ or _managers_.

In the frontend module we export a default object that is an InversifyJS `ContainerModule` with bindings for a command contribution and a menu contribution. Please see our dependency injection guide for more details.

```typescript
export default new ContainerModule(bind => {
    // add your contribution bindings here
    bind(CommandContribution).to(HelloWorldCommandContribution);
    bind(MenuContribution).to(HelloWorldMenuContribution);
});
```

A command is a plain data structure defining an ID and a label. The behaviour of a command is implemented by registering a handler to its ID in a command contribution. The generator has already added a command and a handler that shows a "Hello World!" message.

```typescript
export const HelloWorldCommand = {
    id: 'HelloWorld.command',
    label: "Shows a message"
};

@injectable()
export class HelloWorldCommandContribution implements CommandContribution {

    constructor(
        @inject(MessageService) private readonly messageService: MessageService,
    ) { }

    registerCommands(registry: CommandRegistry): void {
        registry.registerCommand(HelloWorldCommand, {
            execute: () => this.messageService.info('Hello World!')
        });
    }
}
...
```

Note how we use `@inject` in the constructor to get the `MessageService` as a property, and how we use that later in the implementation of the handler. This is the elegance of dependency injection: As a client, we neither care where these dependencies come from nor what their lifecycle is.

To make it accessible by the UI, we implement a `MenuContribution`, adding an item to the Search/Replace section of the edit menu in the menu bar.

```typescript
...
@injectable()
export class HelloWorldMenuContribution implements MenuContribution {

    registerMenus(menus: MenuModelRegistry): void {
        menus.registerMenuAction(CommonMenus.EDIT_FIND, {
                commandId: HelloWorldCommand.id,
                label: 'Say Hello'
            });
    }
}
```

## Adding Extensions to a Griffin Analytics Studio application

To make sure your extension is included in your Griffin Analytics Studio application, list it as a dependency in your browser or electron app, e.g. like this:

```json
{
  "private": true,
  "name": "browser-app",
  "version": "0.0.0",
  "dependencies": {
    "@theia/core": "latest", 
    ...
    "hello-world": "0.0.0"
  },
  "devDependencies": {
    "@theia/cli": "latest" 
  },
  "scripts": {
    "bundle": "yarn rebuild && theia build --mode development", 
    "rebuild": "theia rebuild:browser --cacheRoot ..", 
    "start": "theia start", 
    "watch": "yarn rebuild && theia build --watch --mode development" 
  },
  "theia": {
    "target": "browser"
  }
}
```
*(Note: Dependencies like `@theia/core`, `@theia/cli` and scripts like `theia build` might need updating later to reflect Griffin-specific packages/commands if they exist)*

## Deploying the Extension

To run the extension, you have two options:
1. Have your extension as part of a monorepo containing a Griffin Analytics Studio-based application importing your extension (like the structure created by the Yeoman Generator)
2. Publish the extension with `yarn publish` and consume it from your Griffin Analytics Studio-based application

See *Executing the Browser Application* and *Executing the Extension in Electron* for more details for adding extensions to the dependencies of a Griffin Analytics Studio-based application and running it.
