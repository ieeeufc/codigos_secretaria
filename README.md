Estes códigos servem para mapear a presença dos nossos membros nas reuniões gerais. Nessas reuniões, nós atualizamos os membros sobre o que está sendo feito no Ramo, dentro dos comitês, nos subgrupos e qualquer outra informação importante. <br>

Sobre o código, foi uma maneira de conseguirmos mapear nossas reuniões, descobrindo quem são os membros com maior e menor frequência e qual foi a aderência da reunião. Assim, é possível analisar sobre membros do grupo e a satisfaçam deles e assim traçar planos para combater qualquer problema. <br>

O uso desses códigos é bem simples e específico para nossa ata da reunião geral, pois tudo começa nela. Elas são feitas no Overleaf e têm o objetivo de registrar o que foi informado de maneira sucinta, com informações técnicas e os repasses de todo o grupo. No topo da da ata, está descrito quem esteve presente na reunião e quem não. <br>

![image](https://github.com/user-attachments/assets/2afae210-9775-4e7e-ad6a-5b9dfa37b507)

Á esquerda, está o Editor com o código onde apresenta todos os membros do Ramo e o comando \textcolor para colocar sua ausência na reunião, à direita o Visualizador com o resultado do código. <br>

Para fazer o mapeamento das reuniões em questão, primeiro precisa-se primeiro coletar os dados de cada reunião, colocando o nome, data da reunião e presença em uma planilha só, e para isso usa-se o código CONVERSOR. Basicamente, ele vai receber o código do Editor do Overleaf mostrado acima e transformar em uma planilha em um formato específico. Em seguida, é só copiar o conteúdo dessa planilha e colocar numa planilha principal, onde será armazenada a presença em todas as reuniões.<br>

Desta maneira, um arquivo tem o registro de todas as reuniões, sinalizando quem estava nas reuniões durante certo período. No entanto, é uma péssima forma para visualizar isso, por isso foi criado um código que organiza esses dados de uma maneira mais agradável, o código DADOS, que utiliza a biblioteca Pandas para pegar o dados dessa planilha principal e fornecer dados filtrados.<br>

![image](https://github.com/user-attachments/assets/2314417c-7e1a-4b8c-88a6-2a619b9c0e5d)

O código fornece essas 4 opções para visualização dos dados <br>

Cada código será melhor explicado no README.md de sua pasta.
