from pcs.cli.common.errors import CmdLineInputError
from pcs.cli.constraint import command
from pcs.cli.reports.output import deprecation_warning
from pcs.common.reports import constraints


def create_with_set(lib, argv, modifiers):
    """
    create colocation constraint with resource set
    object lib exposes library
    list argv see usage for "constraint colocation set"
    dict like object modifiers can contain
        "force" allows resource in clone/master and constraint duplicity

    Options:
      * --force - allow resource inside clone (or master), allow duplicate
        element
      * -f - CIB file
    """
    modifiers.ensure_only_supported("-f", "--force")
    command.create_with_set(
        lib.constraint_colocation.create_with_set,
        argv,
        modifiers,
    )


def show(lib, argv, modifiers):
    deprecation_warning(
        "This command is deprecated and will be removed. "
        "Please use 'pcs constraint colocation config' instead."
    )
    return config_cmd(lib, argv, modifiers)


def config_cmd(lib, argv, modifiers):
    """
    show all colocation constraints
    object lib exposes library
    list argv see usage for "constraint colocation show"
    dict like object modifiers can contain "full"

    Options:
      * --full - print more details
      * -f - CIB file
    """
    modifiers.ensure_only_supported("-f", "--full")
    if argv:
        raise CmdLineInputError()
    print(
        "\n".join(
            command.config_cmd(
                "Colocation Constraints:",
                lib.constraint_colocation.config,
                constraints.colocation_plain,
                modifiers,
            )
        )
    )
