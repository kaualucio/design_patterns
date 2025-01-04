# Factory Method (Método Fábrica)

## O que é?
É um padrão de projeto criacional que permite a criação de objetos a partir de uma superclasse (um objeto mais geral e que abrange mais itens, exemplo: Veículo) mas que também permite que a subclasses (uma classe mais específica do que a superclasse, exemplo: Carro) alterem o tipo de objetos a serem criados

## Qual problema resolve?
Resolve principalmente o problema de instanciar objetos sem acoplar o código ao tipo da classe que está sendo instânciada. 
Exemplo: Um serviço de lógistica que trata apenas da logística de Caminhões, se só trata desse tipo de logística toda a logíca da aplicação se concentrará na classe Caminhão. Caso você queira adicionar a logistica marítma, por exemplo, seria necessário uma grande alteração na base do código.

## Qual a solução que o factory method trás?
O factory method sugere que pare de instanciar objetos diretamente através do operador **new** e passe a fazer isso através do method *fábrica* especial da classe. Elas ainda são criadas atráves do operador **new** porém pelo método da fábrica.

## Quando usar o factory method
* Use quando precisar criar objetos de tipos que variar, e esses tipos só podem ser conhecidos em definidos em tempo de execução, ou seja, quando você não sabe quais serão as classes e objetos criados antes do código executar.
* Use o Factory Method quando deseja economizar recursos do sistema reutilizando objetos existentes em vez de recriá-los sempre.
* Use caso você esteja criando uma biblioteca ou framework e quer que seus usuários ou desenvolvedores que utilizem sua ferramenta possam customizar o comportamento dos objetos sem a necessidade de alterar diretemente o código-fonte da biblioteca ou framework.