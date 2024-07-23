# Introdução

Como criar um projeto com poetry?

```s
poetry new intro python
```

Como ativar o ambiente virtual do projeto onde estarão os pacotes utilizados nele:

Crie o arquivo chamado `poetry.toml` e dentro escreva:

```s
[virtualenvs]
in-project=true
```

Para ativar o ambiente digite:

```s
poetry shell
```

Para desativar:

```s
deactivate
```

Para saber se esta ativo:

```s
which python
```

```s
dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ poetry shell
Spawning shell within /home/dali/github.com/intro_python/.venv
dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ . /home/dali/github.com/intro_python/.venv/bin/activate
(intro-python-py3.10) dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ which python
/home/dali/github.com/intro_python/.venv/bin/python
(intro-python-py3.10) dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ deactivate
dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ which python
dali@DESKTOP-C2QA8H1:~/github.com/intro_python$ 
```

Como instalar um pacote:

```s
poetry shell
poetry add playwright
```


Comonado para gravar o codigo playwright
```s
playwright codegen --target python -o 'consulta_site_lago.py' -b chromium https://yodelportal.com/buntzen-lake/Half-Day-Pass
```