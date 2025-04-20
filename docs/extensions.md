---
title: Extensions
---

# Extensions and Plugins

Griffin Analytics Studio is designed in a very modular and extensible way. It supports four ways of being extended/adapted to your specific requirements. These are complementary and are targeted at different use cases. You can pick the best option and even mix them within the same project.
In the following, we will give you a quick overview of the available extension mechanisms and provide more details in the sections below.

- **VS Code extensions**: Simple to write, installable at runtime, compatible with VS Code, limited to the VS Code extension API, some use cases not possible due to API restrictions => Used for adding features to existing tools. Note that you can also use existing VS Code extensions within Griffin Analytics Studio, too.
- **Griffin Analytics Studio extensions**: Install at compile time, full access to internals of Griffin Analytics Studio via dependency injection, almost no limitations in terms of accessible API => used to build custom products and for features not covered by the VS Code extension API. Note that the Griffin Analytics Studio project (including the core) is fully built using Griffin Analytics Studio extensions in a modular way.
- **Griffin Analytics Studio plugins**: Like VS Code extensions, additional access to some Griffin Analytics Studio specific APIs and the Frontend (frontend plugins), Griffin Analytics Studio specific parts are not compatible with VS Code.
- **Headless plugins**: Like VS Code extensions, simple to write and installable at runtime, but extending and interacting only with the Griffin Analytics Studio backend services. These are not scoped to frontend connections and have no access (directly) to frontend services.

The following diagram shows the high level architecture for all four options. VS Code extensions and Griffin Analytics Studio plugins run in a dedicated process per frontend connection, can be installed at runtime, and work against a defined API. Headless plugins similarly run in a dedicated process, but only one that is not associated with any frontend connection. Griffin Analytics Studio extensions are added during compile time and become a core part of your Griffin Analytics Studio application. They can access the full API of Griffin Analytics Studio.

If you would like more guidance on which mechanism to use, please also refer to a detailed comparison between VS Code extensions and Griffin Analytics Studio extensions.

## VS Code Extensions

VS Code extensions are the popular mechanism to extend VS Code with new language support and other features. VS Code extensions are simple to develop and they have access to a defined and restricted API. VS Code extensions can be pre-installed (built in), but also installed at runtime (e.g. by the user). Griffin Analytics Studio provides the same extension API as VS Code, so extensions are compatible. Therefore, to develop your own extension, please refer to the VS Code extension documentation. Please also refer to the coverage report, highlighting which API of VS Code is covered by Griffin Analytics Studio.
Please also note that you can use existing VS Code extensions in Griffin Analytics Studio, too. A good source for installing or downloading extensions is the Open VSX registry.

## Griffin Analytics Studio Extensions

A Griffin Analytics Studio extension is a module that resides inside a Griffin Analytics Studio application and directly communicates with other modules (Griffin Analytics Studio extensions). The Griffin Analytics Studio project itself is composed of Griffin Analytics Studio extensions too. To create a Griffin Analytics Studio application, you can select a number of Griffin Analytics Studio extensions provided by the Griffin Analytics Studio project (core extensions), add your own custom Griffin Analytics Studio extensions and then compile and run the result. Your custom Griffin Analytics Studio extension will have access to the same API as the core extensions. This modularity allows you to extend, adapt or remove almost anything in Griffin Analytics Studio according to your requirements. Also, specific use cases, such as complex views are easier to develop with Griffin Analytics Studio extensions compared to VS Code extensions.
Technically, an extension is an npm package that exposes any number of DI modules (`ContainerModule`) that contribute to the creation of the DI container.
Extensions are consumed by declaring them as a `dependency` in the `package.json` of the application/extension, and are installed at compile time.
See the relevant section for more detail on how to author a Griffin Analytics Studio extension.

## Griffin Analytics Studio Plugins

Griffin Analytics Studio plugins are a special type of VS Code extensions that only run in Griffin Analytics Studio. They share the architecture and other attributes of VS Code extensions, but they also have access to additional API that is only available in Griffin Analytics Studio, not in VS Code. Most noticeable, Griffin Analytics Studio plugins can also directly contribute to the frontend while VS Code extensions are restricted to the backend. As a consequence Griffin Analytics Studio plugins can directly manipulate the UI without going through a webview abstraction, easing the development process. Please be aware that the support for Griffin Analytics Studio Plugins is currently under discussion. We therefore recommend using VS Code extensions or Griffin Analytics Studio extensions instead of Griffin Analytics Studio Plugins.

## Headless Plugins

Headless plugins are a special type of plugin that only runs in Griffin Analytics Studio. They are very similar architecturally and otherwise to VS Code extensions, except that they run in the Node backend outside of the scope of any frontend connection. Therefore, they are suitable for extensibility use cases involving CLI interactions where there is no browser frontend and extension of common backend services defined for application-specific purposes. Accordingly, they are not provided with a default API for access to the backend Griffin Analytics Studio services but have access only to custom APIs published explicitly to them by the application to support the extensibility of its own backend services.
