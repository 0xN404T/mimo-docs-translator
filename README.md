# MiMo Docs Translator

MiMo Docs Translator is a Markdown documentation translation tool powered by Xiaomi MiMo API.

## Problem
Open-source projects often lack multilingual documentation. Indonesian, English, and Chinese developers may struggle to use tools if docs are only available in one language.

## Solution
This CLI translates technical Markdown while preserving headings, lists, and code blocks. It helps developers create localized docs quickly.

## Core Features
- Markdown input support
- Target language selection
- Code block preservation prompt
- CLI usage
- MiMo API integration

## Architecture
1. User provides Markdown file
2. CLI reads content
3. MiMo translates content with formatting rules
4. CLI prints translated Markdown
5. Output can be redirected into a new file

## Example Use Case
Translate `README.md` into Indonesian:
```bash
python translate.py README.md Indonesian > README.id.md
```

## Files
- `translate.py` — translator CLI
- `requirements.txt` — Python dependencies

## Roadmap
- Batch folder translation
- Frontmatter preservation
- Glossary support
- Automatic docs site generation
- Pull request automation

## Why Xiaomi MiMo
MiMo can support multilingual technical documentation workflows for global developer communities.

## Project Maturity
- MVP code available
- Architecture documented
- Roadmap documented
- CI configured
- MIT licensed

## Links
- [Architecture](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)
- [Examples](examples/basic.md)
