---
name: Sempre fazer commit após cada pedido
description: Garante que a versão atual do projeto seja sempre salva no git antes de novas alterações complexas.
---

# Regra: Commit a cada pedido
Sempre que concluir um pedido do usuário e antes de começar a editar arquivos para uma nova solicitação, você DEVE rodar um comando git para commitar as alterações feitas. 
Isso garante que o usuário tenha um ponto de restauração seguro caso as mudanças não fiquem boas ou quebrem o layout.

## Como proceder
Execute algo como:
`git add . && git commit -m "feat: <resumo das alterações concluídas>"`

E só depois avise o usuário que concluiu a tarefa.
