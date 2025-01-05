# Abstract Factory Method (Método de Fábrica Abstrata)

## O que é?
O Abstract Factory é um padrão que fornece uma interface para criar famílias de objetos relacionados ou dependentes. Em vez de instanciar objetos diretamente, delegamos a criação para uma "fábrica" abstrata e suas implementações concretas.

## Qual problema resolve?
Esse padrão resolve o problema de manter a consistência entre objetos que pertencem à mesma família e de evitar a dependência direta de classes concretas no código.

## Qual a solução que o factory method trás?
O Abstract Factory oferece uma solução estruturada para a criação de famílias de objetos relacionados ou interdependentes, eliminando a necessidade de o código cliente conhecer as classes concretas utilizadas. Em vez disso, a criação dos objetos é delegada a uma fábrica abstrata, que é implementada de forma concreta para atender a diferentes contextos ou configurações. Isso garante que os objetos criados sejam consistentes e compatíveis entre si, permitindo que o sistema seja facilmente expandido com novas famílias sem alterar o código existente.

## Quando usar o factory method
* Quando precisar criar objetos relacionados ou interdependentes e deseja garantir que eles sejam usados em conjunto (ex.: botões e checkboxes de um tema específico).
* Quando quer ou precisa isolar o código cliente das classes concretas, facilitando futuras mudanças ou expansões.
* Quando o sistema precisa ser escalável para novas famílias de objetos sem grandes refatorações.
