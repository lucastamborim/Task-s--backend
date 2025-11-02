## Registro de Desenvolvimento – Backend

## Estudo e planejamento

Inicialmente, li a documentação oficial do Django, Django REST Framework e Djoser.

Assisti a vídeos tutoriais no YouTube para entender melhor a criação de APIs REST com autenticação JWT.

Objetivo dessa etapa: planejar a modelagem das entidades e entender o fluxo de autenticação seguro.

## Modelagem e implementação inicial

Enfrentei dificuldades na modelagem do usuário, pois criar um modelo compatível com JWT era mais complexo do que o esperado.

Pedi ajuda ao ChatGPT e foi recomendado utilizar o User model nativo do Django, o que simplificou bastante o desenvolvimento.

Com isso, implementei o modelo Tarefa e seus serializers, incluindo validações de campos obrigatórios (título, descrição e tipo).

## Desenvolvimento de autenticação e endpoints

Configurei o Djoser com JWT para cadastro, login, refresh e verificação de tokens.

Surgiram problemas em algumas rotas que deveriam ser públicas (login, criação de conta, recuperação de senha) e estavam exigindo token.

Busquei soluções em vídeos mais recentes no YouTube e consegui ajustar as permissões para que essas rotas funcionassem corretamente sem autenticação.

##  Finalização e testes

Finalizei os ViewSets, filtros por status e tipo, e ordenação por data de criação.

Testei todos os endpoints usando Postman.

Implementei testes básicos com python manage.py test.

Concluí o backend pouco antes da metade do prazo total (prazo de 3 semanas), garantindo que todos os requisitos da API estivessem atendidos.

## Uso de IA

O ChatGPT foi consultado principalmente para:

Sugestões sobre modelagem de usuários compatível com JWT.

Boas práticas de organização de serializers e ViewSets.

*Todas as sugestões foram avaliadas criticamente e adaptadas para a realidade do projeto.