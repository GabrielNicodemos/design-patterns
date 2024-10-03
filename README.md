# Repositório de Padrões de Projeto

Este repositório tem como objetivo fornecer uma implementação prática de diversos padrões de projeto em Python. A ideia é facilitar o aprendizado e a compreensão dos padrões através de exemplos claros e concisos. Cada padrão de projeto é implementado de forma a demonstrar sua aplicação em cenários do mundo real.

## Padrões de Projeto Incluídos

- **[Strategy](#strategy)**: Permite definir uma família de algoritmos, encapsulá-los e torná-los intercambiáveis.
- **[Singleton](#singleton)**: Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância.
- **[Chain Responsability](#chain-of-responsibility)**: Define uma cadeia de objetos responsáveis por tratar uma solicitação.
- **[Decorator](#decorator)**: Permite adicionar comportamento a um objeto dinamicamente. [EM ANDAMENTO]
- **[Adapter](#adapter)**: O Adapter converte a interface de uma classe em outra interface que o cliente espera. Ele permite que classes com interfaces incompatíveis trabalhem juntas.
- **Observer**: Define uma dependência um-para-muitos entre objetos, de forma que quando um objeto muda de estado, todos os seus dependentes são notificados. [EM ANDAMENTO]
- **Factory Method**: Define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. [EM ANDAMENTO]

## Propósito, ganho e situações de uso de cada padrão de projeto

### *Strategy*
#### Propósito
O padrão de projeto Strategy é como ter várias estratégias em um jogo. Em vez de ter uma única maneira de fazer algo, você pode escolher entre diferentes estratégias com base na situação.
#### Ganho no uso
1. **Separação de Responsabilidades**:
    - Cada algoritmo é encapsulado em sua própria classe, seguindo o princípio da responsabilidade única. Isso facilita a manutenção e a legibilidade do código.
2. **Facilidade de Manutenção**:
    - Alterações em uma estratégia específica não afetam outras estratégias ou a lógica do contexto, reduzindo o risco de introduzir bugs ao modificar o código.
3. **Flexibilidade**:
    - Você pode adicionar novas estratégias sem modificar o código existente. Isso permite que o sistema evolua facilmente para atender novas necessidades.
4. **Reutilização de Código**:
    - Estratégias podem ser reutilizadas em diferentes partes da aplicação ou em diferentes aplicações, economizando tempo de desenvolvimento.
5. **Simplicidade no Contexto**:
    - O contexto permanece leve e simples, sem a necessidade de ter lógica complexa para escolher e implementar algoritmos.
#### Situações de uso
1. **Múltiplos Algoritmos para um Problema**:
    - Quando você tem um problema que pode ser resolvido por diferentes algoritmos ou estratégias, e a seleção do algoritmo pode mudar em tempo de execução.
2. **Mudanças Frequentes de Algoritmos**:
    - Quando a aplicação precisa permitir que os algoritmos mudem frequentemente ou que novas estratégias sejam adicionadas ao longo do tempo.
3. **Evitando Condicionais Excessivas**:
    - Quando você se depara com muitas instruções `if` ou `switch` que selecionam um algoritmo com base em alguma condição. O padrão Strategy ajuda a evitar esse tipo de lógica complexa.
4. **Facilidade de Testes**:
    - Cada estratégia pode ser testada independentemente, facilitando a criação de testes unitários e a validação de cada algoritmo isoladamente.
5. **Alterações Independentes**:
    - Quando diferentes equipes ou desenvolvedores podem estar trabalhando em diferentes estratégias ao mesmo tempo, minimizando os conflitos de fusão em projetos colaborativos.
------
### *Singleton*
#### Propósito
O Singleton é um padrão de projeto criacional que permite a você garantir que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância.
#### Ganho no uso
1. Consistência Global: Garante que há apenas uma instância de uma classe, promovendo um estado global consistente em toda a aplicação.
2. Gerenciamento de Recursos: Ideal para gerenciar recursos limitados, como conexões de banco de dados ou arquivos de configuração, evitando a sobrecarga de criar múltiplas instâncias.
3. Facilidade de Acesso: Proporciona um ponto de acesso global, facilitando a obtenção da instância única de qualquer lugar da aplicação.
4. Controle de Estado: Permite que o estado mantido na instância única seja compartilhado entre diferentes partes da aplicação, evitando a duplicação de dados.
5. Evita Conflitos: Reduz a chance de conflitos de estado, pois a mesma instância é utilizada em vez de várias instâncias que podem ter estados diferentes.
#### Situações de uso
1. **Conexões de Banco de Dados**: Quando você precisa garantir que apenas uma conexão ao banco de dados esteja ativa em toda a aplicação, evitando múltiplas conexões desnecessárias.
2. **Gerenciamento de Configurações**: Para armazenar configurações globais que devem ser acessadas por diferentes partes da aplicação, como parâmetros de configuração de sistema.
3. **Logger**: Um sistema de logging que deve ter uma única instância para garantir que todas as mensagens sejam registradas em um único lugar.
4. **Cache**: Para implementar um sistema de cache que deve ser compartilhado entre diferentes partes da aplicação, evitando a duplicação de dados.
5. **Gestores de Recursos**: Para gerenciar acesso a recursos limitados, como impressoras ou pools de threads, garantindo que o acesso seja controlado e eficiente.
6. **Fábricas de Objetos**: Em alguns casos, um padrão de fábrica pode se beneficiar de ser um Singleton para garantir que todos os objetos criados sejam geridos de maneira uniforme.
------
### *Chain of Responsibility*
#### Propósito
O padrão de projeto **Chain of Responsibility** (Cadeia de Responsabilidade) é um padrão comportamental que permite que um pedido ou comando seja processado por uma cadeia de manipuladores, onde cada manipulador decide se processa o pedido ou o passa para o próximo na cadeia. Isso permite que o remetente de um pedido não precise saber qual manipulador, ou objeto, será responsável por tratá-lo.
### Como funciona?
- O pedido passa por uma sequência de objetos (manipuladores), cada um podendo processar o pedido ou encaminhá-lo ao próximo.
- O padrão promove o desacoplamento entre o remetente do pedido e os objetos que o processam, possibilitando que novos manipuladores sejam adicionados sem alterar o código que envia o pedido.
#### Ganho no uso
1. **Desacoplamento**: O cliente (remetente do pedido) não precisa saber qual objeto da cadeia processará o pedido.
2. **Flexibilidade**: Os manipuladores podem ser reordenados ou alterados sem impacto no código que faz o pedido.
3. **Manutenção facilitada**: Novos manipuladores podem ser adicionados à cadeia sem modificar os existentes.
4. **Responsabilidade distribuída**: Em vez de um único objeto manipular todo o processamento, a responsabilidade pode ser dividida entre diferentes objetos.
#### Situações de uso
1. **Diversos possíveis manipuladores**: Quando um pedido pode ser tratado por diferentes objetos, mas não se sabe qual deles será responsável.
2. **Manutenção e extensibilidade**: Quando deseja-se tornar o sistema fácil de estender, adicionando novos manipuladores sem modificar o código existente.
3. **Validação de dados**: Em sistemas onde diversas validações precisam ser aplicadas sequencialmente, como em formulários complexos.
4. **Sistemas de autorização**: Onde várias regras e níveis de permissão precisam ser aplicados para acessar certos recursos.
5. **Tratamento de erros**: Onde diferentes tipos de erros são tratados por manipuladores diferentes.
---
### *Decorator*
#### Propósito
O padrão Decorator é um padrão de design estrutural que permite adicionar funcionalidades a objetos de maneira dinâmica, sem alterar o código original da classe do objeto. Ele envolve a criação de uma série de "decoradores", que são essencialmente invólucros ao redor de objetos que modificam ou estendem seu comportamento.
#### Ganho no uso
1. **Extensibilidade**: Você pode adicionar ou remover funcionalidades a um objeto de forma dinâmica, sem alterar a classe original nem criar subclasses.
2. **Flexibilidade**: Como decoradores são aplicados dinamicamente, você pode combinar várias funcionalidades ao objeto de forma modular, criando diferentes combinações de comportamento sem alterar a estrutura do código existente.
3. **Separação de Preocupações**: Funcionalidades adicionais podem ser isoladas em diferentes classes decoradoras, mantendo o código mais organizado e fácil de manter.
4. **Reuso de Código**: Ao evitar subclasses para cada variação de comportamento, o código dos decoradores pode ser reutilizado com diferentes objetos.
5. **Evita Subclasse Explosiva**: Sem o decorador, para cada combinação possível de comportamentos, seria necessário criar uma nova subclasse, resultando em um grande número de subclasses. O Decorator evita esse crescimento descontrolado.
#### Situações de uso
1. **Adicionar Comportamentos Dinâmicos**: Quando você precisa adicionar funcionalidades a objetos em tempo de execução, como diferentes formas de notificação (e-mail, SMS, push notifications).
2. **Modificar Comportamentos de Objetos**: Quando há necessidade de modificar o comportamento de um objeto sem alterar a sua classe base, como adicionar log, autenticação, ou compressão a uma classe de processamento de dados.
3. **Evitar Múltiplas Subclasses**: Quando a criação de várias subclasses para diferentes combinações de comportamento geraria complexidade desnecessária. Por exemplo, em um sistema de envio de pedidos onde você quer aplicar descontos de forma condicional e flexível.
4. **Imitação de Funções Adicionais**: Quando objetos compartilham uma interface comum, mas precisam de variações sutis de comportamento. Por exemplo, sistemas de streaming de música, onde pode-se aplicar diferentes filtros de áudio.
---
### *Adapter*
#### Propósito
O padrão Adapter é um padrão de design estrutural que permite que interfaces incompatíveis trabalhem juntas, convertendo a interface de uma classe existente em outra interface que o cliente espera. O Adapter age como um intermediário, adaptando uma classe ou sistema existente para uma nova interface sem modificar seu código original.
#### Ganho no uso
1. **Compatibilidade**: O **Adapter** permite que componentes de software que não foram projetados para trabalhar juntos possam interagir, adaptando a interface de um componente para que ele possa ser usado por outro.
2. **Reuso de Código Existente**: O **Adapter** facilita o reaproveitamento de código existente que não pode ser alterado diretamente (por exemplo, classes de bibliotecas externas) ao fornecer uma interface compatível com o sistema atual.
3. **Flexibilidade**: Permite adaptar diferentes sistemas ou classes sem a necessidade de modificações complexas ou criação de novas classes, mantendo a estrutura original intacta.
4. **Isolamento de Mudanças**: Você pode introduzir mudanças em um sistema externo ou legado sem precisar alterar as interfaces ou o código que já depende dele. Isso é especialmente útil em projetos com componentes antigos.
5. **Facilita Integração de Sistemas Legados**: É ideal para integrar sistemas antigos com novas soluções sem reescrever o código legado.
#### Situações de uso
1. **Integração com Sistemas Legados**: Quando você precisa usar uma classe de um sistema legado (ou uma biblioteca de terceiros) em um novo sistema que espera uma interface diferente. O **Adapter** converte a interface antiga para a nova interface sem a necessidade de alterar o código legado.
2. **Compatibilidade entre APIs**: Quando você está migrando para uma nova API e quer adaptar a nova API para funcionar com código antigo. O **Adapter** pode mapear os métodos da nova API para os métodos esperados pelo cliente antigo.
3. **Sistemas de Terceiros**: Quando você precisa integrar sistemas de fornecedores externos que têm interfaces diferentes das que o seu sistema utiliza. O **Adapter** ajusta a interface fornecida pelo sistema externo para se adequar ao que você precisa.
4. **Interfaces Incompatíveis**: Se você tem duas classes com interfaces diferentes que precisam trabalhar juntas (por exemplo, uma classe antiga que usa métodos diferentes das novas), o **Adapter** pode harmonizar as duas.
---
Author: Gabriel Eduardo C. Nicodemos
