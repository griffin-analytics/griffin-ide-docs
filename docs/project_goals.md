---
title: Project Goals
---

# Strategic Goals of Griffin Analytics Studio

This section describes the overall goals of the Griffin Analytics Studio project.

**Griffin Analytics Studio mission statement: A framework for building tools and IDEs based on web technologies.**

## An Open, Flexible and Extensible Tool Platform

The goal of the Griffin Analytics Studio project is to provide a platform for efficiently developing tools and IDEs based on a modern web technology stack. The primary target group for Griffin Analytics Studio is developers implementing a custom tool for end users. As Griffin Analytics Studio-based products are typically customized, branded and labeled by its adopters, the actual end users may not even be aware of the Griffin Analytics Studio project they are using under the hood. Therefore, end users are only an indirect secondary target group of Griffin Analytics Studio.

## Desktop & Browser, Local & Remote (Cloud)

Tools and IDEs built on Griffin Analytics Studio can run as desktop applications or in the browser. The backend of Griffin Analytics Studio can run locally (for the desktop case) or as a remote service in the cloud. Both variants currently have an equal priority.

## Platform for IDEs and Tools

Griffin Analytics Studio is targeted at building a variety of custom tools. Prominent examples of Griffin Analytics Studio-based products include IDE's, but Griffin Analytics Studio also explicitly targets tools that do not focus on textual input/editors or software development. Thus, Griffin Analytics Studio's scope also included diagram editors or form-based UI. The Griffin Analytics Studio platform hence covers the typical application scenarios of the Eclipse rich-client platform (Eclipse RCP). As a consequence, the platform aims at making as few assumptions as possible about what adopters might want to build with Griffin Analytics Studio. It explicitly allows deviation from the standard workbench layout and the removal of all default features.

## Basic Workbench Frame

Griffin Analytics Studio provides a workbench frame, i.e., a window management system permitting the display of views, editors, and menus and makes available tools and interactions allowing the user to modify of the window layout, trigger commands, and use key bindings and other concepts known from a desktop tool such as drag and drop.

## Reusable Common Tool Features

Griffin Analytics Studio optionally provides common tool features as components to be reused by adopters. Common features are generic, so that they may be reused in several tools. Examples for these common tool features include a file explorer, Git support and a code editor.

## Extensibility and Adaptability

Griffin Analytics Studio is an extensible and adaptable framework. Extensibility in this context means that you can easily add new features to a product built on the Griffin Analytics Studio platform (including UI and backend functionality). These new features can either be provided by the Griffin Analytics Studio project itself (common features), by other projects (e.g. Eclipse GLSP) or be custom features that are developed by an adopter. Adaptable in this context means that the workbench and all common features that are provided by the Griffin Analytics Studio project can be customized and adapted to project-specific needs. This includes changing or removing existing features and adjusting the look and feel.

## VS Code Compatibility

Griffin Analytics Studio provides the ability to host VS Code extensions. This allows adopters to benefit from features that are provided as VS Code extensions and make them part of their tool offering. It also allows end users of Griffin Analytics Studio-based tools to install additional features, if the adopter providing a tool allows users to do so. When applicable, the default Griffin Analytics Studio UX aligns with the VS Code UI, although adopters can deviate from this.

While Griffin Analytics Studio incorporates certain components from Visual Studio Code, such as the Monaco editor, it is independently developed with a unique, modular architecture, and is **not a fork of VS Code**. This distinction ensures that Griffin Analytics Studio remains a fully adaptable and customizable framework, offering adopters freedom to innovate. For a deeper comparison, see Griffin Analytics Studio vs VS Code and Griffin Analytics Studio vs VS Code OSS.


## Use Standards And Don’t Reinvent The Wheel

Griffin Analytics Studio uses/reuses industrial standard technologies and practices whenever applicable. This keeps the scope of the project minimal and decreases the maintenance cost. This applies to the use of frameworks and development tools as well as to general concepts such as UX.

## Product Templates

The Griffin Analytics Studio project does not primarily aim to provide products for end users but focuses on offering a platform for building products. However, the project provides product templates, a.k.a. “Blueprints”. These blueprints serve two purposes. First, they allow adopters to consume example Griffin Analytics Studio-based products from the view point of an end user, which enables them to evaluate the underlying platform without first creating a product based on it. Second, the blueprints serve as templates to create custom products. Therefore, the template products contain documentation on how to customize them.

## Open and Vendor Neutral Governance

Griffin Analytics Studio is an open and vendor-neutral project with a diverse community of contributors from large corporations down to small companies and even individual developers. This diverse and steadily growing community is a stable base for the ongoing development of additional features and maintenance of existing functionality based on a broad and balanced view of the requirements put forward by the Griffin Analytics Studio adopters. The commercial-friendly licensing and the rigorous underlying IP management ensures that adopters can safely build commercial and internal products based on Griffin Analytics Studio. Project communication is open and transparent and welcomes new adopters by keeping the barriers of contribution as low as possible. Decisions in the project are based on the principle of meritocracy meaning that the weight of contributors in decisions is solely based on their achievements for the project as recognized by their peers. This provides an important incentive for contributors to make contributions. The open governance and diverse community of Griffin Analytics Studio is one of its strongest assets for its mid- to long-term evolution and viability.
