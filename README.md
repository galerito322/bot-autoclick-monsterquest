# bot-autoclick-monsterquest

# Bot para fazer o modo ADVENTURE de forma semi-automatizada (resumo)

- Precisa instalar o python e algumas bibliotecas 
- Ideal pra quem tem vários monstros e não quer dar 20x12x3 clicks (obs: caso pra quem tem 20 monstros) quando eles estão com a stamina full.
- Um monstro deve ser selecionado manualmente ao iniciar o bot e ao termino de sua stamina, é configurado dessa forma para que ele não ataque com monstros indesejáveis (obs: deixe os botões de FIGHT disponíveis na tela de forma manual no primeiro loop e no termino da stamina de cada monstro) 
- Caso algum passo não esteja funcionando corretamente basta realizar a substituição da imagem na pasta do bot por outra equivalente (obs: matenha o mesmo nome da imagem substituída). Você pode fazer isso usando as teclas (Windows+shift+s) ou qualquer outra coisa que possibilite o recorte da imagem, ex: paint ou lightshot.
- Sim, copiei parte do tutorial de instalação do python do bot do bombercrypto

# Video demonstrativo de uso
https://www.youtube.com/watch?v=nS-dzYHtHaU

# Instalação:
### Baixe e instale o Python pelo [site](https://www.python.org/downloads/) ou pela [windows store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab).

Se você baixar pelo site é importante marcar a opção para adicionar o
python ao PATH:
![1_add_path](https://user-images.githubusercontent.com/58611244/151722169-ff4eee79-4d90-465b-84a9-14a727512667.png)

### Realize o download do codigo no formato zip, e extraia o arquivo.

### Copie o caminho até a pasta do bot:

![2_way](https://user-images.githubusercontent.com/58611244/151722173-7c05af95-fd58-4722-92ef-5e52d8f19bdd.png)

### Abra o terminal e navegue até a pasta do bot:
Digite o comando "cd" + caminho que você copiou:

![3_way_prompt](https://user-images.githubusercontent.com/58611244/151722174-ad70c688-6007-49c6-8db5-202095102454.png) 

### Instale as dependências:

```
pip install -r requirements.txt
```
  
![4_requirements](https://user-images.githubusercontent.com/58611244/151722175-470d51fb-a4db-4215-849f-aaf6575f78a8.png)

### Pronto! Agora é só iniciar o bot com o comando

```
python3 index.py
```

![5_run_py](https://user-images.githubusercontent.com/58611244/151722176-c6cc07ef-4c24-4052-ba53-93093de033ce.png)

# Como usar?

Abra o terminal, se ainda não tiver navegado para a pasta do bot dê novamente o comando

```
"cd" + caminho que você copiou
```

Para iniciar use o comando 

```
python3 monsterquest.py
```

Ou simplismente vá até a pasta e abra o arquivo monsterquest.py 

# Como o bot funciona?

Ao iniciar o bot pressione enter dentro do terminal para que ele começe a busca

![1_finding_for_img](https://user-images.githubusercontent.com/58611244/151724009-8e69a80e-380c-498e-8df1-64ac406ac5db.png)

Eu sugiro que a tela do terminal fique dividida para melhor acompanhamento das informações. Você pode fazer isso com as teclas (Windows + setas de direcionamento)

![4_suggestion](https://user-images.githubusercontent.com/58611244/151724015-51f1b005-d576-4b8f-9f3f-3b7639b41ee9.png)

Quando o bot é iniciado ou quando a stamina de algum monstro acaba ele faz a busca pelos 3 botões de FIGHT e clicka no primeiro monstro que até então é o que sempre tem a maior porcentagem de vitória (obs: deixe os botões de FIGHT disponíveis na tela de forma manual no primeiro loop e no final do loop de cada monstro) 

![2_found_buttons](https://user-images.githubusercontent.com/58611244/151724012-6c80ea25-d003-4fe3-8f38-447f59eeea3d.png)

Ná próxima tela ele verifica as opções de ataque e prioriza sempre o botão SKILL ATTACK caso o mesmo esteja disponível

![3_found_second_buttons](https://user-images.githubusercontent.com/58611244/151724014-b67f1056-1441-4812-bd6e-047105ae7889.png)






