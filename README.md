Isto é um script simples que fará o envio de mensagens no WhatsApp de números de uma lista, utilizando selenium.webdriver e webdriver_manager.

Problemas que o script possivelmente irá enfrentar;

1 - Quedas de conexão ou conexões muito lentas podem ser fatais, em caso de conexões lentas deverá aumnetar o tempo de espera do script.
2 - Navegadores com anuncios pop-up serão quase fatais, resolva os proibindo de exibir anúncios.

Precauções tomadas pelo script;

1 - Seguir tentando enviar as mensagens em caso de números inválidos.
2 - Seguir a risca todos os passos em todos os números, ou seja, sempre começar pelo começo.
3 - Ser o mais "humano" possível, afim de parecer um humano qualquer, ou seja, sem flood de requesições.

- Use o Chrome na versão 99 para ter pleno funcionamento. sinta-se livre para testar em outras versões.
- Este script se destina a pequenas empresas que precisem enviar mensagens para vários clientes de forma automática.
- Uma vez conectado não haverá mais a necessidade de manter o telefone conectado à internet, pelo menos até então.
- Críticas construtivas são bem vindas :)