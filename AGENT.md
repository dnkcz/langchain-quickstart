# Setup

## Create virtual environment

```bash
python -m venv .venv
```

## Activate virtual environment

```bash
.\.venv\Scripts\activate
```

## Install pip-tools

```bash
python -m pip install --upgrade pip
python -m pip install pip-tools
```

## Compile dependencies

```bash
python -m piptools compile requirements.in
```

## Install compiled dependencies

```bash
python -m pip install -r requirements.txt
```
