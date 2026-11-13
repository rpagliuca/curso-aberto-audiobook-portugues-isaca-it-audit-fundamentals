# curso-aberto-audiobook-portugues-isaca-it-audit-fundamentals

Curso aberto, em português, para estudar para o certificado **ISACA IT Audit Fundamentals** ouvindo: no carro, na caminhada, na academia.

**▶ Ouvir agora: https://rpagliuca.github.io/curso-aberto-audiobook-portugues-isaca-it-audit-fundamentals/**

Feito no mesmo formato do [curso aberto da ISO 27001 Lead Implementer](https://github.com/rpagliuca/curso-aberto-audiobook-portugues-iso-27001-lead-implementer).

## O que tem (e o que está em produção)

- **Conteúdo**: 10 seções de até 10 minutos, uma para cada 10% da prova, com resumo, quiz e transcrição completa por seção.
  Executar a auditoria (35%) ocupa quatro seções; ambiente de TI (25%), três; função de auditoria e controles e riscos (13%),
  temas específicos (15%) e tecnologias novas (12%), uma cada.
- **Perguntas e respostas** (em produção): cerca de 1 hora em capítulos de ~8 minutos, no formato
  *pergunta → silêncio para responder → resposta*.
- **Simulado diagnóstico** (em produção): 20 questões com nota por domínio.
- **Player feito para dirigir**: os botões avançar/voltar do Bluetooth do carro ou do fone pulam 10 s e atravessam as seções
  como uma faixa contínua; ao terminar uma seção a próxima começa sozinha; a posição é retomada ao reabrir a página.

## A prova

Online com fiscal remoto, 2 horas, aprovação com 65%. Domínios e pesos, segundo a ISACA: Performing an Audit 35%,
IT Environment and Components 25%, Specific Audit Subjects 15%, Overview of Newer Technologies 12%,
Controls, Risk and Audit 8%, Audit Function 5%.

## O texto é o código-fonte

Todo áudio é artefato gerado a partir de texto versionado aqui. Para revisar ou corrigir, edite o texto, nunca o MP3.

| Conteúdo | Fonte | Gerador |
|---|---|---|
| Seções | `roteiro/sNN-*.md` (blocos `## Narração`, `## Resumo`, `## Quiz`) | `gerar_audio.py` |
| Pronúncia | `pronuncia.py` (siglas soletradas com pontos; termos em inglês em grafia fonética) | usado pelo `gerar_audio.py` |
| Site (GitHub Pages, `docs/`) | `site/template.html` + roteiros | `gerar_site.py` |

```bash
python gerar_audio.py s01      # precisa de edge-tts e ffmpeg; cache em .tts-cache/
python gerar_site.py           # reescreve docs/index.html
python3 serve.py               # serve docs/ em 127.0.0.1:8742, com HTTP Range
```

A voz é a `pt-BR-AntonioNeural` do edge-tts (serviço online da Microsoft), a 10% mais rápida. O serviço às vezes devolve
`NoAudioReceived` para um texto que funciona segundos depois; o gerador tenta de novo com espera crescente.

## Fontes

Síntese própria, escrita a partir de material de estudo de auditoria de sistemas (a base é o CISA Review Manual da ISACA)
e das páginas públicas da ISACA sobre o certificado. Nenhum trecho de livro é reproduzido aqui.

Material independente, sem vínculo com a ISACA. IT Audit Fundamentals, CISA e ITAF são marcas da ISACA.
