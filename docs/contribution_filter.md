---
title: Contribution Filter
---

# Contribution Filter

The Contribution Filter feature in Griffin Analytics Studio enables developers to remove specific contributions from a Griffin Analytics Studio-based application. This capability is typically used to eliminate existing features already present in Griffin Analytics Studio core, such as specific commands or menu entries.

For a general understanding of contributions and contribution points, please refer to the Services and Contributions documentation.

## Overview

The Contribution Filter feature provides a way to selectively disable certain contributions within a Griffin Analytics Studio application. This is handled by the `ContributionFilterRegistry` and `FilterContribution`s,  which allow you to register and apply filters to contributions.

### FilterContribution API

The `FilterContribution` interface allows you to register your contribution filters. These filters will be used by the `ContributionFilterRegistry` to remove or modify contributions.

- **registerContributionFilters(registry: ContributionFilterRegistry): void**
  - Use this method to register your contribution filters with the `ContributionFilterRegistry`.

## Example Usage

Here's an example of how to use the Contribution Filter to remove specific commands from a Griffin Analytics Studio application. In this example, we will first define some commands and the filter them. If you want to filter some existing contributions, you would of course skip the first step and just provide a `FilterContribution`.

### Step 1: Define Example Commands and implement Command Contributions

First, we define an example command that we want to filter out (more information about commands).

```typescript
import { Command } from '@theia/core/lib/common';

export namespace SampleFilteredCommand {

    const EXAMPLE_CATEGORY = 'Examples';

    export const TO_BE_FILTERED: Command = {
        id: 'example_command.filtered',
        category: EXAMPLE_CATEGORY,
        label: 'This command should be filtered out'
    };
}
```
*(Note: Import path `@theia/core` kept as technical detail)*

We register the example command with a command contribution.

```typescript
import { CommandContribution, CommandRegistry } from '@theia/core/lib/common';
import { injectable } from 'inversify';

@injectable()
export class SampleFilteredCommandContribution implements CommandContribution {

    registerCommands(commands: CommandRegistry): void {
        commands.registerCommand(SampleFilteredCommand.TO_BE_FILTERED, { execute: () => { } });
    }
}
```
*(Note: Import path `@theia/core` kept as technical detail)*

### Step 2: Register Filters

Now, we register the filters to remove specific contributions, in our case the example command we just registered. The filter below is scoped to be only applied to `CommandContribution`, you can use '*' to filter any type of contribution. In the filter implementation, we additionally check for the specific type `SampleFilteredCommandContribution` in the example.

```typescript
import { FilterContribution, ContributionFilterRegistry, CommandContribution } from '@theia/core/lib/common';
import { injectable } from 'inversify';

@injectable()
export class SampleFilterContribution implements FilterContribution {

    registerContributionFilters(registry: ContributionFilterRegistry): void {
        registry.addFilters([CommandContribution], [
            contrib => !(contrib instanceof SampleFilteredCommandContribution)
        ]);
    }
}
```
*(Note: Import path `@theia/core` kept as technical detail)*

### Step 3: Bind Contributions

Ensure that your contributions are properly bound in the dependency injection container.

```typescript
import { interfaces } from 'inversify';
import { CommandContribution, bindContribution } from '@theia/core/lib/common';

export function bindSampleFilteredCommandContribution(bind: interfaces.Bind): void {
    bind(CommandContribution).to(SampleFilteredCommandContribution).inSingletonScope();
    bind(FilterContribution).to(SampleFilterContribution).inSingletonScope();
}
```
*(Note: Import path `@theia/core` kept as technical detail)*

## Summary

The Contribution Filter feature in Griffin Analytics Studio is a powerful tool for developers to manage and customize the contributions in their applications. By leveraging `FilterContributions` , developers can easily define and apply filters to remove or modify specific contributions, thereby tailoring the functionality of their Griffin Analytics Studio-based applications to their specific needs.
