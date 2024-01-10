"""Summaries a source code file.

sample command:
python -m summarize "sample_code.py"
"""

import sys

from tree_sitter import Language, Parser

Language.build_library(
    # Store the library in the `build` directory
    "build/my-languages.so",
    # Include one or more languages
    [
        "tree-sitter-python",
    ],
)


def get_language(filename):
    """Infers the programming language based on filename extension."""
    extension = filename.split(".")[-1]
    if extension == "py":
        return Language("build/my-languages.so", "python")
    # Add more language mappings here based on extensions (e.g., "java", "cpp")
    else:
        raise ValueError(f"Unsupported language for file: {filename}")


def get_summary(filename):
    """Parses the source code and generates a summary."""
    language = get_language(filename)
    parser = Parser()
    parser.set_language(language)

    with open(filename) as f:
        source_code = f.read()

    tree = parser.parse(source_code.encode("utf-8"))

    def get_imported_libraries(language, tree):
        query = language.query("""
        (import_statement (dotted_name)@name)
        """)
        return [
            node.text.decode() for node, tag in query.captures(tree.root_node)
        ]

    def get_defined_functions(language, tree):
        query = language.query("""
        (function_definition (identifier) @name)
        """)
        return [
            node.text.decode() for node, tag in query.captures(tree.root_node)
        ]

    def get_defined_classes(language, tree):
        query = language.query("""
        (class_definition (identifier) @name)
        """)
        return [
            node.text.decode() for node, tag in query.captures(tree.root_node)
        ]

    libraries = get_imported_libraries(language, tree)
    functions = get_defined_functions(language, tree)
    classes = get_defined_classes(language, tree)

    summary = f"""
  File Summary for: {filename}

  - Imported {len(libraries)} Libraries: {", ".join(libraries)}
  - Defined {len(functions)} Functions: {", ".join(functions)}
  - Defined {len(classes)} Classes: {", ".join(classes)}
  """

    return summary


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    summary = get_summary(filename)
    print(summary)
