
## Como criar um ambiente virtual:

#### 1º

Criando o ambiente virutal
```
python -m venv venv
```


Ativar o ambiente virtual
```
.\nomedoambiente\Scripts\activate
```


### Caso dê errado com o erro de policy


Abra o powershell como admin e execute o comando 

```
Set-ExecutionPolicy Unrestricted -Force
```
Volte ao VSCODE e feche e abra novamente
e execute o primeiro passo

### 2 º maneira

Caso dê erro do ambiente virutal não ser reconhecido, você terá que baixar
Semelhante ao erro abaixo:
```
Error: Command '['C:\\Windows\\system32\\env\\Scripts\\python.exe', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
```

#### Em seu terminal do VS code digite:
```
pip install virtualenv
```


Criar o novo ambiente virtual com o virtualenv em vez do env


```
virtualenv nomedoambiente
```

E por fim execute o ambiente
```
.\nomedoambiente\Scripts\activate
```



Se você estiver utilizando o gitbash como terminal padrão 


source ./nomedoambiente/Scripts/activate



