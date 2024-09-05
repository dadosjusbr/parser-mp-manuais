CONTRACHEQUE_MPPA = "contracheque-mppa"
INDENIZACOES_MPPA = "indenizacoes-mppa"
CONTRACHEQUE_MPRJ = "contracheque-mprj"
INDENIZACOES_MPRJ = "indenizacoes-mprj"
INDENIZACOES_MPRJ_10_2022 = "indenizacoes-mprj-10-2022"
INDENIZACOES_MPRJ_05_2023 = "indenizacoes-mprj-05-2023"
INDENIZACOES_MPRJ_07_2023= "indenizacoes-mprj-07-2023"
CONTRACHEQUE_MPRN = "contracheque-mprn"
INDENIZACOES_MPRN = "indenizacoes-mprn"
CONTRACHEQUE_MPTO = "contracheque-mpto"
INDENIZACOES_MPTO = "indenizacoes-mpto"
CONTRACHEQUE_MPPE = "contracheque-mppe"
INDENIZACOES_MPPE = "indenizacoes-mppe"
CONTRACHEQUE_MPPI = "contracheque-mppi"
INDENIZACOES_MPPI = "indenizacoes-mppi"
CONTRACHEQUE_MPSP = "contracheque-mpsp"
INDENIZACOES_MPSP = "indenizacoes-mpsp"
CONTRACHEQUE_MPAC = "contracheque-mpac"
INDENIZACOES_MPAC = "indenizacoes-mpac"
CONTRACHEQUE_MPAL = "contracheque-mpal"
INDENIZACOES_MPAL = "indenizacoes-mpal"
CONTRACHEQUE_MPBA = "contracheque-mpba"
INDENIZACOES_MPBA = "indenizacoes-mpba"
CONTRACHEQUE_MPES = "contracheque-mpes"
INDENIZACOES_MPES_01_2021 = "indenizacoes-mpes-01-2021"
INDENIZACOES_MPES_02_2021 = "indenizacoes-mpes-02-2021"
INDENIZACOES_MPES_04_2021 = "indenizacoes-mpes-04-2021"
INDENIZACOES_MPES_08_2021 = "indenizacoes-mpes-08-2021"
INDENIZACOES_MPES_12_2021 = "indenizacoes-mpes-12-2021"
CONTRACHEQUE_MPSE = "contracheque-mpse"
INDENIZACOES_MPSE = "indenizacoes-mpse"
CONTRACHEQUE_MPRR = "contracheque-mprr"
INDENIZACOES_MPRR = "indenizacoes-mprr"

HEADERS = {
    CONTRACHEQUE_MPPA: {
        "REMUNERAÇÃO BÁSICA": {
            "Remun. do Cargo Efetivo (1)": 4,
            "Outras Verbas Remuneratórias ou Legais/Judiciais (2)": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de confiança ou Cargo em Comissão (3)": 6,
            "Gratif. Natalina (4)": 7,
            "Férias (1/3 Const.) (5)": 8,
            "Abono de Permanência (6)": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contr. Previdenciária (10)": 13,
            "Imposto de Renda (11)": 14,
            "Retenção p/ teto constitucional (12)": 15,
            "Outros Descontos": 16,
        },
    },
    INDENIZACOES_MPPA: {
        "AUXÍLIO AUXILIO ALIMENTACAO": 7,
        "AUXÍLIO AUXILIO-SAUDE": 8,
        "VANTAGEM DEV. V. ALIMENTACAO": 9,
        "VANTAGEM DEA - AUXILIO-SAUDE": 10,
        "REMUNERAÇÃO DIF DE CONVOCACAO": 12,
        "REMUNERAÇÃO DIFERENCA PROMOCAO": 13,
        "VANTAGEM DEV. DESC. FALTAS": 14,
        "VANTAGEM DEV. DESC. ATRASOS": 15,
        "GRATIFICAÇÃO COMPL. SALARIAL": 16,
        "GRATIFICAÇÃO ACUMUL15%-LEI7736/13": 17,
        "GRATIFICAÇÃO ACUMUL20%-LEI7736/13": 18,
        "GRATIFICAÇÃO ACUMUL25%-LEI7736/13": 19,
        "DIFERENCA DE SUBSTITUICAO DIF DE SUBSTITUICAO": 20,
        "ADICIONAL ADIC.PERICULOSIDADE": 21,
        "ADICIONAL ADIC INSALUBRIDADE": 22,
    },
    CONTRACHEQUE_MPRJ: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do cargo efetivo": 4,
            "Outras verbas remuneratórias, legais ou judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de confiança ou cargo em comissão": 6,
            "Gratificação natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição previdenciária": 13,
            "Imposto de renda": 14,
            "Retenção por teto constitucional": 15,
        },
    },
    INDENIZACOES_MPRJ: {
        "AUXÍLIO-ALIMENTAÇÃO - 1": 4,
        "AUXÍLIO-EDUCAÇÃO - 1": 5,
        "AUXÍLIO-SAÚDE - 1": 6,
        "DEVOLUÇÃO IR RRA": 7,
        "INDENIZAÇÃO DE FÉRIAS NÃO USUFRUÍDAS": 8,
        "INDENIZAÇÃO POR LICENÇA NÃO GOZADA": 9,
        "AUXÍLIO-ALIMENTAÇÃO": 10,
        "AUXÍLIO-EDUCAÇÃO": 11,
        "AUXÍLIO-SAÚDE": 12,
        "DEVOLUÇÃO FUNDO DE RESERVA": 13,
        "DIFERENÇAS DE AUXÍLIOS": 14,
        "GRATIFICAÇÕES EVENTUAIS": 15,
        "INDENIZAÇÃO DE TRANSPORTE": 16,
        "PARCELAS PAGAS EM ATRASO": 17,
    },
    INDENIZACOES_MPRJ_10_2022: {
        "AUXÍLIO-ALIMENTAÇÃO - 1": 4,
        "AUXÍLIO-EDUCAÇÃO - 1": 5,
        "AUXÍLIO-SAÚDE - 1": 6,
        "CONVERSÃO DE LICENÇA ESPECIAL/PRÊMIO": 7,
        "INDENIZAÇÃO DE FÉRIAS NÃO USUFRUÍDAS": 8,
        "INDENIZAÇÃO DE TRANSPORTE - 1": 9,
        "INDENIZAÇÃO POR LICENÇA NÃO GOZADA": 10,
        "AUXÍLIO-ALIMENTAÇÃO": 11,
        "AUXÍLIO-EDUCAÇÃO": 12,
        "DIFERENÇAS DE AUXÍLIOS": 13,
        "GRATIFICAÇÕES EVENTUAIS": 14,
        "INDENIZAÇÃO DE TRANSPORTE": 15,
        "PARCELAS PAGAS EM ATRASO": 16,
    },
    INDENIZACOES_MPRJ_05_2023: {
        "AUXÍLIO-ALIMENTAÇÃO - 1": 4,
        "AUXÍLIO-EDUCAÇÃO - 1": 5,
        "AUXÍLIO-SAÚDE - 1": 6,
        "INDENIZAÇÃO DE FÉRIAS NÃO USUFRUÍDAS": 7,
        "INDENIZAÇÃO DE TRANSPORTE - 1": 8,
        "INDENIZAÇÃO POR LICENÇA NÃO GOZADA": 9,
        "AUXÍLIO-ALIMENTAÇÃO": 10,
        "AUXÍLIO-EDUCAÇÃO": 11,
        "AUXÍLIO-SAÚDE": 12,
        "DIFERENÇAS DE AUXÍLIOS": 13,
        "GRATIFICAÇÕES EVENTUAIS": 14,
        "INDENIZAÇÃO DE TRANSPORTE": 15,
        "PARCELAS PAGAS EM ATRASO": 16,
    },
    INDENIZACOES_MPRJ_07_2023: {
        "AUXÍLIO-ALIMENTAÇÃO - 1": 4,
        "AUXÍLIO-EDUCAÇÃO - 1": 5,
        "AUXÍLIO-SAÚDE - 1": 6,
        "CONVERSÃO DE LICENÇA ESPECIAL/PRÊMIO": 7,
        "INDENIZAÇÃO DE FÉRIAS NÃO USUFRUÍDAS": 8,
        "INDENIZAÇÃO DE TRANSPORTE - 1": 9,
        "INDENIZAÇÃO POR LICENÇA NÃO GOZADA": 10,
        "AUXÍLIO-ALIMENTAÇÃO": 11,
        "AUXÍLIO-EDUCAÇÃO": 12,
        "AUXÍLIO-SAÚDE": 13,
        "DIFERENÇAS DE AUXÍLIOS": 14,
        "GRATIFICAÇÕES EVENTUAIS": 15,
        "INDENIZAÇÃO DE TRANSPORTE": 16,
        "PARCELAS PAGAS EM ATRASO": 17,
    },
    CONTRACHEQUE_MPRN: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional": 15,
            "Descontos diversos": 16,
        },
    },
    INDENIZACOES_MPRN: {
        "Auxílio Saúde": 4,
        "Auxílio Alimentação": 5,
        "Auxílio Moradia": 6,
        "Substituição Cargo C. Função GAE": 7,
        "Adicional Periculosidade": 8,
        "Licença Compensatória": 9,
    },
    CONTRACHEQUE_MPTO: {
        "REMUNERAÇÃO BÁSICA": {
            "REMUNERAÇÃO DO CARGO EFETIVO": 4,
            "OUTRAS VERBAS REMUNERATÓRIAS, LEGAIS OU JUDICIAIS": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "FUNÇÃO DE CONFIANÇA OU CARGO EM COMISSÃO": 6,
            "GRATIFICAÇÃO NATALINA": 7,
            "FÉRIAS CONSTITUCIONAIS": 8,
            "ABONO DE PERMANÊNCIA": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "CONTRIBUIÇÃO PREVIDENCIÁRIA": 10,
            "IMPOSTO DE RENDA": 11,
            "RETENÇÃO POR TETO CONSTITUCIONAL": 12,
        },
    },
    INDENIZACOES_MPTO: {
        "Auxílio-Alimentação": 4,
        "Auxílio-Moradia": 5,
        "Férias Indenizadas": 6,
        "Licença Prêmio Indenizada": 7,
        "Programa de Aposentadoria Incentivada": 8,
        "Verbas Rescisórias": 9,
        "Cumulação": 10,
        "Complemento por Entrância": 11,
    },
    CONTRACHEQUE_MPPE: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional": 15,
        },
    },
    INDENIZACOES_MPPE: {
        "0053-L PREM S/TRB": 4,
        "0243-AUX TRANSP": 5,
        "0261-AUX MORADIA": 6,
        "0269-AUX REFEICAO": 7,
        "0270-AUX ALIM": 8,
        "0272-AUX SAUDE": 9,
        "0098-ABON PER ATR": 10,
        "0201-DIF ENTRANC": 11,
        "0244-ADC SERV EXT": 12,
        "0251-SERV EXT PLT": 13,
        "0265-IND FERIAS": 14,
        "0267-ADC AT ESPEC": 15,
        "0271-GRT SUB FGMP": 16,
        "0275-AD EXERCICIO": 17,
        "0279-ADIC PR/TEMP": 18,
        "0400-VENCIM ATR": 19,
        "0401-DIF ENTR ATR": 20,
        "0403-QUINQ ATR": 21,
        "0408-AB FER PR AT": 22,
        "0416-PENS AL ATR": 23,
        "0420-INDZ ASS ATR": 24,
        "0425-INDZ DIR ATR": 25,
        "0426-13 SAL ATR": 26,
        "0429-INDZ COO ATR": 27,
        "0434-AD L16307 AT": 28,
        "0435-SUBSIDIO ATR": 29,
        "0443-AUX TRP ATR": 30,
        "0444-AD SV EX ATR": 31,
        "0451-SV EX PL ATR": 32,
        "0459-COM LIC ATR": 33,
        "0463-A FERIAS ATR": 34,
        "0467-AD AT ES ATR": 35,
        "0469-AUX REF ATR": 36,
        "0470-AUX ALIM ATR": 37,
        "0471-GR SU FG ATR": 38,
        "0472-AUX SAUDE AT": 39,
        "0475-ADIC EXE ATR": 40,
        "0479-AD PR/TP ATR": 41,
        "0480-GRT FGMP ATR": 42,
        "0483-IN CGSMP ATR": 43,
        "0486-IND OUV ATR": 44,
        "0497-IND CGPG ATR": 45,
        "522 ATS.TRIBUTAV": 46,
        "523 ATS.N.TRIBUT": 47,
        "558 PAE NTRB ATR": 48,
        "559 PAE TRIB ATR": 49,
        "563 VAN.EXER.ATU": 50,
        "564 VAN.EXER.ANT": 51,
    },
    CONTRACHEQUE_MPPI: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias Constitucionais": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional": 15,
        },
    },
    INDENIZACOES_MPPI: {
        "AUXÍLIO ALIMENTAÇÃO": 4,
        "AUXÍLIO SAÚDE": 5,
        "ABONO PECUNIÁRIO": 6,
        "INDENIZAÇÃO POR CUMULAÇÃO": 7,
        "COMPLEMENTO POR ENTRÂNCIA": 8,
    },
    CONTRACHEQUE_MPSP: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 Constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional": 15,
        },
    },
    INDENIZACOES_MPSP: {
        "Auxílio Alimentação": 4,
        "Férias em Pecúnia": 5,
        "Licença Prêmio em Pecúnia": 6,
        "Assistência Saúde": 7,
        "Gratificação Cumulativa": 8,
        "Gratificação de Natureza Especial": 9,
        "Gratificação de Grupo de Atuação Especial": 10,
    },
    CONTRACHEQUE_MPAC: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 5,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 6,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 7,
            "Gratificação Natalina": 8,
            "Férias (1/3 constitucional)": 9,
            "Abono de Permanência": 10,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 14,
            "Imposto de Renda": 15,
            "Retenção por Teto Constitucional": 16,
            "OUTROS": 17,  # desconto
        },
    },
    INDENIZACOES_MPAC: {
        "AUXILIO ALIMENTACAO MEMBROS": 4,
        "AUXILIO ALIMENTACAO SERVIDORES": 5,
        "AUXILIO ALIMENTACAO RETROATIVO": 6,
        "AUXILIO SAUDE SERVIDORES": 7,
        "AUXILIO SAUDE PENSAO": 8,
        "AUXILIO SAUDE RETROATIVO SERVIDORES": 9,
        "AUXILIO SAUDE SERVIDORES APOSENTADOS": 10,
        "AUXILIO SAUDE": 11,
        "GRAT POR ACUMULACAO DE CARGOS E FUNCOES": 12,
        "DIF INCOR TRIBUTADA EXERCICIO ANTERIOR": 13,
        "CONT PREV ESTADUAL RETIDO A MAIOR": 14,
        "DIFERENCA POR SUBSTITUICAO": 15,
        "GRAT POR ACUM DE CARGOS/FUNCOES RETRO": 16,
        "ABONO DE PERMANENCIA RETROATIVO": 17,
        "PAE TRIBUTADO": 18,
        "CC PROPORCIONAL": 19,
    },
    # Algumas rubricas do MPAL aparece em ambas planilhas
    CONTRACHEQUE_MPAL: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 3,
            "Outras Verbas Remuneratórias": 4,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            # "Acervo Processual": 5,
            "Função de Confiança ou CC": 6,
            "Grat. Natalina": 7,
            "Férias / Terço Constitucional": 8,
            "Abono de Permanência": 10,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 11,
            "Imposto de Renda": 12,
            "Teto Constitucional (10)": 13,
        },
        # "Auxílio Saúde": 14,
        # "Auxílio Alimentação": 15,
        "VERBAS INDENIZATÓRIAS": {
            "Auxílio Transporte": 16,
            "Auxílio Moradia": 17,
            "Férias Indenizadas": 18,
            "Férias Indenizadas Estágio": 19,
            # "Insalubridade": 20,
            # "Remuneração Lei 6773": 21,
            # "Remuneração Lei 6818": 22,
            # "Diferença de Entrância": 23,
            "Rem. Lei 6773 / Ato 09/2012": 24,
        },
        # "Rem. Ato 11/2018": 25,
        # "Coord. de Grupos de Trabalho": 26,
        # "Comissões e Projetos": 27,
        # "Rem. de Chefia/Dir/Assessoria": 28,
    },
    INDENIZACOES_MPAL: {
        "Auxilio Saúde": 4,
        "Acumulo Acervo Processual": 5,
        "Auxílio Alimentação": 6,
        "Férias Indenizadas Ativos": 7,
        "Férias Indenizadas": 8,
        "Remuneração Ato 11/2018": 9,
        "Insalubridade": 10,
        "Remuneração Lei 6773": 11,
        "Remuneração Lei 6818": 12,
        "Diferença de Entrância": 13,
        "Coordenação de Grupos de Trabalho": 14,
        "Participação em Comissões e Projetos": 15,
        "Remuneração de Chefia/Direção/Assessoria": 16,
    },
    CONTRACHEQUE_MPBA: {
        "REMUNERAÇÃO BÁSICA": {
            "Remuneração do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional": 15,
        },
    },
    INDENIZACOES_MPBA: {
        "Auxílio-alimentação": 4,
        "Auxílio-transporte": 5,
        "Auxílio-Moradia": 6,
        "Auxílio-natalidade": 7,
        "Substituição Membros": 8,
        "Ajuda de Custo": 9,
        "Serviço Extraordinário": 10,
        "Substituição de Função": 11,
        "Gratificação de Serviços Especiais": 12,
        "Diferença de Entrância": 13,
    },
    CONTRACHEQUE_MPES: {
        "REMUNERAÇÃO BÁSICA": {
            "Remunerção do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional CONSTITUCIONAL": 15,
        },
    },
    # 01, 03 de 2021
    INDENIZACOES_MPES_01_2021: {
        "CARTÃO ALIMENTAÇÃO": 4,
        "AUXÍLIO-SAÚDE": 5,
        "PLANTÃO": 6,
    },
    # 02, 07 de 2021
    INDENIZACOES_MPES_02_2021: {
        "CARTÃO ALIMENTAÇÃO": 4,
        "ABONO FÉRIAS INDENIZATÓRIAS": 5,
        "AUXÍLIO-SAÚDE": 6,
        "PLANTÃO": 7,
    },
    # 04, 05, 06, 09, 10, 11 de 2021
    INDENIZACOES_MPES_04_2021: {
        "CARTÃO ALIMENTAÇÃO": 4,
        "FÉRIAS INDENIZATÓRIAS": 5,
        "FÉRIAS PRÊMIO": 6,
        "AUXÍLIO-SAÚDE": 7,
        "PLANTÃO": 8,
    },
    # 08 de 2021
    INDENIZACOES_MPES_08_2021: {
        "CARTÃO ALIMENTAÇÃO": 4,
        "FÉRIAS INDENIZATÓRIAS": 5,
        "ABONO FÉRIAS INDENIZATÓRIAS": 6,
        "FÉRIAS PRÊMIO": 7,
        "AUXÍLIO-SAÚDE": 8,
        "PLANTÃO": 9,
    },
    # 12 de 2021
    INDENIZACOES_MPES_12_2021: {
        "CARTÃO ALIMENTAÇÃO": 4,
        "FÉRIAS INDENIZATÓRIAS": 5,
        "FÉRIAS PRÊMIO": 6,
        "AJUDA DE CUSTO": 7,
        "AUX. MORADIA": 8,
        "AUXÍLIO-SAÚDE": 9,
        "PLANTÃO": 10,
    },
    CONTRACHEQUE_MPSE: {
        "REMUNERAÇÃO BÁSICA": {
            "Remunerção do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional CONSTITUCIONAL": 15,
        },
    },
    INDENIZACOES_MPSE: {
        "Auxílio Saúde": 4,
        "Dif. Auxílio-Saúde": 5,
        "Auxílio-Alimentação": 6,
        "Dif. Auxílio-Alimentação": 7,
        "Auxílio-Interiorização": 8,
        "Dif. Auxílio-Interiorização": 9,
        "Auxílio Educ. Infantil - TJSE": 10,
        "Dif. Auxílio Educ. Infantil - TJSE": 11,
        "Indenizações Férias/Licença-Prêmio": 12,
        "Abono Pecuniário": 13,
        "Dif. Abono Pecuniário": 14,
        "Ressarcimentos": 15,
        "Ajuda de Custo": 16,
        "Dif. GEO": 18,
        "Insalubridade": 19,
        "Dif. Insalubridade": 20,
        "Periculosidade": 21,
        "Dif. Periculosidade": 22,
        "Adicional Trabalho Técnico": 23,
        "Dif. Adicional Trabalho Técnico": 24,
        "Grat. Atividade Ensino": 25,
        "Substituições": 26,
        "Dif. Substituições": 27,
        "Cumulação": 28,
        "Dif. Cumulação": 29,
        "Representação de Direção": 30,
        "Dif. Representação de Direção": 31,
        "Grat. Turma Recursal": 32,
        "Dif. Grat. Turma Recursal": 33,
        "Grat. Difícil Provimento": 34,
        "Dif. Grat. Difícil Provimento": 35,
        "Grat. Assessor": 36,
        "Dif. Grat. Assessor": 37,
        "Representação GAECO": 38,
        "Dif. Representação GAECO": 39,
        "Gratificação Diretor Subsede": 40,
        "Dif. Gratificação Diretor Subsede": 41,
        "Grat. por Acumulação de Acervo": 42,
        "Dif. Grat. por Acumulação de Acervo": 43,
    },
    CONTRACHEQUE_MPRR: {
        "REMUNERAÇÃO BÁSICA": {
            "Remunerção do Cargo Efetivo": 4,
            "Outras Verbas Remuneratórias, Legais ou Judiciais": 5,
        },
        "REMUNERAÇÃO EVENTUAL OU TEMPORÁRIA": {
            "Função de Confiança ou Cargo em Comissão": 6,
            "Gratificação Natalina": 7,
            "Férias (1/3 constitucional)": 8,
            "Abono de Permanência": 9,
        },
        "OBRIGATÓRIOS/LEGAIS": {
            "Contribuição Previdenciária": 13,
            "Imposto de Renda": 14,
            "Retenção por Teto Constitucional CONSTITUCIONAL": 15,
        },
    },
    INDENIZACOES_MPRR: {
        "Auxílio-Alimentação": 5,
        "Ajuda de Custo para Mudança de Domicílio": 6,
        "Auxílio-Saúde": 7,
        "Férias Indenizadas": 8,
        "Conversão de Licença Acumulação de Acervo": 9,
        "Auxílio Natalidade": 10,
        "Licença Prêmio Indenizada": 11,
        "Ajuda de Custo para Capacitação": 12,
        "Verbas Rescisórias": 13,
        "Auxílio Moradia": 14,
        "Parcela de Irredutibilidade": 15,
        "Gratificação por Substituição Cumulativa": 17,
        "Substituição": 18,
        "Gratificação por Produtividade": 19,
    },
}
