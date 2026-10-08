# Verificação de Conta Git (Vercel)

Se a Vercel bloquear o deploy dizendo "commit author did not have contributing access", significa que o Git do seu computador enviou o código usando um e-mail diferente do que está cadastrado na sua conta Vercel/GitHub.

Para este projeto, o e-mail correto autorizado pela Vercel é:
**`rafaelaliamaduart@gmail.com`**

## Como garantir que está certo

A configuração já foi feita localmente apenas para esta pasta, então não deve atrapalhar seus outros projetos da Asimov. Para verificar se está certo, abra o terminal nesta pasta e rode:

```bash
git config user.email
```
*Deve retornar: `rafaelaliamaduart@gmail.com`*

## Como consertar se der erro de novo

Se por acaso algum commit for com o e-mail errado e a Vercel travar, rode o seguinte comando no terminal (dentro desta pasta) para arrumar o último envio:

```bash
git config user.email "rafaelaliamaduart@gmail.com"
git commit --amend --reset-author --no-edit
git push origin main -f
```
Isso vai reescrever a autoria do código para o e-mail correto e forçar o envio para o GitHub, destravando a Vercel.
