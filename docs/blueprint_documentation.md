---
title: Extending/Adopting Griffin Analytics Studio
---

# Extending/Adopting Griffin Analytics Studio

This guide provides an overview on how to extend and customize Griffin Analytics Studio to your own custom IDE or tool. In this scenario, Griffin Analytics Studio is an example product used as a reference on how to build desktop IDE-like products based on the Griffin Analytics Studio framework. If you just want to use Griffin Analytics Studio, see the user guide.

Please note that adopting Griffin Analytics Studio as a basis is just one of several ways to get started with building a Griffin Analytics Studio-based application. We recommend reading the article "Build your own IDE/Tool" as a first step. Furthermore, this guide is focused on building a desktop app. We also provide an experimental Docker version of Griffin Analytics Studio as an alternative.

Griffin Analytics Studio assembles a selected subset of existing Griffin Analytics Studio features and extensions.
We provide installers for Griffin Analytics Studio to be downloaded.
In the respective git repository you can also find the source code for Griffin Analytics Studio and its installers.

This documentation will use these sources as a template. We will explain
how to customize this template so that you can build your own custom Griffin Analytics Studio-based product including installers and packaging for installing the desktop-based version of your custom product on all major operating systems. Please note that the technical name (e.g. in the source code) for Griffin Analytics Studio is "Theia Blueprint" to avoid confusion with the generic term "IDE".

- Building a product and installers
- Signing
- Adding/removing Features
- Updating Bundled VS Code Extensions
- Customizing Griffin Analytics Studio Extensions
- Branding
- Configure Publish and Update

## Building a product and installers

Griffin Analytics Studio build uses electron-builder to package the product as a desktop application.

The product can be built and packaged with yarn.
Note that you usually can only package the product for the operating system you execute the build on.
For more information see the electron-builder documentation on multi-platform builds.

The following commands may be run from the root directory of the repository.

To install dependencies and build the application, simply execute `yarn`.

You can also directly run the unpackaged application, e.g. to test it during development with `yarn electron start`.

With `yarn electron package`, you package the application into an executable file for your current operating system.
The packaged application will be located in `applications/electron/dist`.
The folder `applications/electron/dist/<OS>-unpackaged` will contain the files that are bundled into the final packaged executable.
For Linux, this is an executable `.AppImage`, for Windows a `.exe` installer, and a `.dmg` disk image for macOS.

You can also just create the unpackaged content by running `yarn electron package:preview`.
This is useful to see the bundled files and saves time compared to a full package.
To publish the current version, the command `yarn electron deploy` can be used.
For more information on publishing also see section "Configure publish and update".

## Signing

Electron-builder supports signing the packaged application on Windows and macOS.
The current signing scripts for Griffin Analytics Studio are located in `applications/electron/scripts`.
The file `after-pack.js` is the current entry point for the configured signing via Eclipse infrastructure.

However, as signing is highly dependent on your setup, see the electron builder’s signing documentation on how to properly set up your own signing.

## Adding/Removing Features

Griffin Analytics Studio is based on the Griffin Analytics Studio platform, which is a flexible and adaptable platform for build tools and IDEs. Therefore, you can adapt the feature set and general appearance of Griffin Analytics Studio to your custom requirements with almost no limits. The Griffin Analytics Studio platform provides two mechanism to add your custom extensions: VS Code extensions and Griffin Analytics Studio extensions. Please have a look at the overview about Griffin Analytics Studio extension capabilities for details. When assembling a product such as Griffin Analytics Studio, you can freely decide, which VS Code extensions and Griffin Analytics Studio extensions are part of it and thereby influence the feature set of your custom product. The following two sections describe how to modify which VS Code Extensions and which Griffin Analytics Studio extensions are part of your product. Please also note that you can allow users of a Griffin Analytics Studio-based tool to install VS Code extensions at runtime.

## Updating Bundled VS Code Extensions

All VS Code extensions that are already included in the product at start-up ("built-ins"), are defined in `applications/electron/package.json`.
They are listed under the `theiaPlugins` property as key-value pairs.
*(Note: `theiaPlugins` property name kept as technical detail)*
The keys can be freely chosen as long as they represent a valid folder name and are unique within the `theiaPlugins` property.
We suggest using the extension’s unique identifier.
The value is the download URL of the extensions.
It will automatically be downloaded during the application’s build process.
Any new plugin will be automatically downloaded the next time one of the following npm scripts is executed:

- `install` (which is the same as just running `yarn`)
- `prepare`
- `download:plugins`

To remove an extension from the product, simply delete its entry.
If plugins were not already downloaded, no further steps are required as downloaded plugins are ignored via gitignore.
However, previously downloaded plugins are not automatically removed.
Therefore, you need to remove its folder from the `applications/electron/plugins` folder.
Alternatively, you can remove the whole `applications/electron/plugins` folder and execute `yarn electron download:plugins` to download all defined plugins.

### Extension sources

We use the Open VSX Registry of the Eclipse Foundation to install extensions.
It is an open and community-driven VS Code extension marketplace.
More information can be found at eclipse.org.

## Customizing Griffin Analytics Studio Extensions

Griffin Analytics Studio extensions can be added through `dependencies` in `applications/electron/package.json`.
Like any other dependency, it will be installed via yarn.
Similarly, removing an extension works by removing it from `dependencies`.
For extensions already published on npm (or your private npm registry) this is all you need to do.

An alternative approach is developing your extension inside Griffin Analytics Studio’s mono repo.
The advantage of doing this is that you don’t need to publish the extension and can build the product with the local version of the extension.
This is facilitated by the lerna build already configured in the Griffin Analytics Studio’s repository.
It links the product and all extensions in the repository together during the build.

The easiest way to create a new extension is to use the official yeoman generator for Griffin Analytics Studio extensions.
Assuming you have yeoman globally installed on your system, simply create a new extension in the repository root with `yo theia-extension --standalone`.
*(Note: `theia-extension` command kept as technical detail)*
The `--standalone` flag is used to only create an extension but not a whole Griffin Analytics Studio application frame because it is already provided by Griffin Analytics Studio.
After successfully generating the extension, add its folder name to the Griffin Analytics Studio’s root `package.json` in the workspaces property.
After adding the extension to the dependencies in `applications/electron/package.json` as described above, the new extension will be part of the built product.

## Branding

You can also add your own branding to the product by customizing the application icons and title, the welcome page and the About dialog.
In addition, some parts of the installer can be customized.

### Customizing the App

#### Application Window Title

The window title is the application’s name if no workspace is opened and `<workspace name> — <application name>` if a workspace is opened.
The application name can be adapted in `applications/electron/package.json` by navigating through the nested properties.

To change the application name, open the file and locate the following nested structure:

```json
  "theia": {
    "frontend": {
      "config": {
        "applicationName": "Griffin Analytics Studio",
      },
    },
  },
```
*(Note: `theia` property name kept as technical detail)*

Change the value of `applicationName` to the desired name.
Also see the structure in the original file.

#### Application Icons

Application icons are located in `applications/electron/resources/`.
Simply replace them with your own icons.
Because each operating system handles icons differently, they should all be replaced to ensure proper use.
They map as follows:

- macOS: icons.icns
- Windows: icon.ico
- Linux: icons subfolder

### Customizing the Welcome Page

The Griffin Analytics Studio welcome page can be customized by binding a custom `WidgetFactory` for Griffin Analytics Studio’s `GettingStartedWidget`.
This is done with Griffin Analytics Studio in the theia-blueprint-product extension.
*(Note: `theia-blueprint-product` kept as technical name)*
The easiest way to customize the welcome page is to adapt the class `TheiaBlueprintGettingStartedWidget` in `theia-extensions/theia-blueprint-product/src/browser/theia-blueprint-getting-started-widget.tsx`.
*(Note: Class name `TheiaBlueprintGettingStartedWidget` kept as technical name)*

The widget is bound in `theia-extensions/theia-blueprint-product/src/browser/theia-blueprint-frontend-module.ts` like this:

```typescript
    bind(TheiaBlueprintGettingStartedWidget).toSelf();
    bind(WidgetFactory).toDynamicValue(context => ({
        id: GettingStartedWidget.ID,
        createWidget: () => context.container.get<TheiaBlueprintGettingStartedWidget>(TheiaBlueprintGettingStartedWidget),
    })).inSingletonScope();
```
*(Note: Class name `TheiaBlueprintGettingStartedWidget` kept as technical name)*

To use another custom widget, remove this code and bind your widget correspondingly.

### Customizing the About Dialog

The Griffin Analytics Studio about dialog can be customized by binding a custom subclass of Griffin Analytics Studio’s `AboutDialog` class to `AboutDialog`.
This is done with Griffin Analytics Studio in the theia-blueprint-product extension.
*(Note: `theia-blueprint-product` kept as technical name)*
The easiest way to customize the about dialog is to adapt the class `TheiaBlueprintAboutDialog` in `theia-extensions/theia-blueprint-product/src/browser/theia-blueprint-about-dialog.tsx`.
*(Note: Class name `TheiaBlueprintAboutDialog` kept as technical name)*

The widget is bound in `theia-extensions/theia-blueprint-product/src/browser/theia-blueprint-frontend-module.ts` like this:

```typescript
isBound(AboutDialog) ? rebind(AboutDialog).to(TheiaBlueprintAboutDialog).inSingletonScope() : bind(AboutDialog).to(TheiaBlueprintAboutDialog).inSingletonScope();
```
*(Note: Class name `TheiaBlueprintAboutDialog` kept as technical name)*

To use another custom dialog widget, remove this code, extend Griffin Analytics Studio’s AboutDialog class, and (re)bind it as above.

### Customizing the Preferences

The default preferences directory in Griffin Analytics Studio is `.theia-blueprint` and is located as described in the Preferences documentation. You can customize this location by modifying `theia-blueprint-variables-server.ts`.
*(Note: Filename `theia-blueprint-variables-server.ts` kept as technical detail)*

### Customizing the Electron Splash Screen

Since Griffin Analytics Studio `1.49.0` Griffin Analytics Studio Electron applications support displaying a splash screen before showing the main window.

The splash screen can be enabled within the application `package.json`'s Griffin Analytics Studio options by providing an object at `theia.frontend.config.electron.splashScreenOptions` with the following properties:
*(Note: `theia.frontend...` path kept as technical detail)*

```typescript
{
    content: string  // <mandatory> path to the content to render within the splash screen, resolved from application root
    width: number // default 640
    height: number // default 480
    minDuration: number // minimum amount of time in milliseconds to show the splash screen before main window is shown. default 0
    maxDuration: number // maximum amount of time in milliseconds before splash screen is removed and main window is shown. default 30000
}
```

If not configured otherwise via `minDuration`, the splash screen will be shown until the frontend is ready, i.e. when the loading spinner is gone.
Then the splash screen will be closed and the main window is shown.

### Showing Windows Early

The main window / splash screen can be configured to be shown "early", i.e. the window will be shown before it's ready to render content.
By default this is `true` to give the user visual feedback as early as possible.

If you prefer only showing the main window / splash screen once they are ready to render content, then you can configure `theia.frontend.config.electron.showWindowEarly: false` in your application's `package.json`.
*(Note: `theia.frontend...` path kept as technical detail)*

### Customizing the Installer

The installers are created using electron-builder.
The corresponding configuration file is located at `applications/electron/electron-builder.yml`.

#### Installer File Base Name

The installer files’ base names are defined by the `productName` property in `applications/electron/electron-builder.yml`.

#### Windows Installer

As is typical for Windows applications, there is an installation wizard for the Windows version of Griffin Analytics Studio.
The installer is configured in the nsis section of the configuration file.
Available customizations include settings such as:

- Icons
- Sidebar image
- License
- One click installation
- Automatic application start after installation
- Whether users can change the installation directory

More details on available options and how they can be customized can be found in the official electron builder documentation.
This documentation also includes information about more advanced features such as custom NSIS scripts.

## Configure Publish and Update

Griffin Analytics Studio uses electron-builder to create and publish installers.
It also uses electron-updater, developed by the electron-builder organization, to provide automatic updates of the installed application.

There are various deployment targets which can be configured in the `applications/electron/package.json` and `applications/electron/electron-builder.yml` as documented in the Electron Builder documentation.
Multiple publish configurations can be configured.
Thereby, the first one is automatically used by the updater to look for available updates.
The currently used generic publishing method does not automatically publish to the specified server, but is just used as the lookup location for the updater.
