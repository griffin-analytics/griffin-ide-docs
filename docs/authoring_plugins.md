---
title: Authoring Plug-ins
---

# Authoring Griffin Analytics Studio Plug-ins

This documentation is deprecated and needs to be updated. We currently recommend using VS Code extensions or Griffin Analytics Studio extensions instead of Griffin Analytics Studio Plugins. See the extension overview for more details.

Let's create our first Griffin plug-in. As an example, we are going to register a command _Hello World_ that displays a notification "Hello world!". This article is guiding you through all the necessary steps.

## Griffin’s Architecture

### Plug-in vs Extension

Griffin is an extensible IDE. You may already have heard extensions as being a way to customize the IDE. Plug-ins is a new extensibility model that has been added recently into Griffin. Here are the main differences between plug-ins vs the extensions.

#### Plug-ins

pros:
 + Code isolation: as plug-in's code in running in separate processes, it can't block Griffin core processes.
 + Can be loaded at runtime. No need to recompile the full IDE of Griffin.
 + Reduce compilation time
 + Self-contained. A plug-in can be packaged into a single file and loaded directly after. No extra need to grab dependencies from npmjs, etc.
 + Simple API
   + No need to learn inversify or any framework.
   + Single entry point, with code completion to see possible calls with associated JsDoc.
 + Upgrade easily from one Griffin version to another version as API is backward compliant.

cons:
 - Need to stick to this pre-defined API. It's not possible to tweak something if contribution point is not provided through API. Note that current API can be extended to support more stuff ;-)

### Design
A Griffin app is composed of a core providing a set of widgets, commands, handlers, etc. for a specific functionality.

Griffin defines a runtime API allowing plug-ins to customize the IDE and add their behaviour to various aspects of the application.

There are two natures of plug-ins:
 - Backend plug-in. If you're familiar with VS Code extensions, it's very close. The plug-in's code is running in its own process on the server side. The API is called and it will send some actions on user's browser/UI to register new commands, etc. All the callbacks are executed on the server side on a dedicated process.
 - Frontend plug-in. In that case, callbacks are executed in a worker thread on the UI/browser. These plug-ins are only authorized to use "browser compliant" modules. For example opening or writing to a file is impossible as all the code of the plug-in is running on the browser side. But this approach is helpful if you really want to have some stuff on the client side to avoid some network operations.


