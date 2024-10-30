# 🤖 Sistema de Controle Inteligente de Pêndulo Invertido

## :bookmark_tabs: Descrição

O projeto desenvolve três diferentes sistemas de controle para estabilizar um pêndulo invertido montado sobre um carro. Cada sistema utiliza técnicas de inteligência computacional para lidar com a complexidade da tarefa de manter o pêndulo na posição vertical. As três abordagens implementadas são:
   - Sistema de Inferência Fuzzy (FIS) - um sistema baseado em lógica fuzzy para controle do pêndulo.
   - Sistema Genético-Fuzzy - uma combinação de algoritmos genéticos e sistema fuzzy para otimização.
   - Sistema Neuro-Fuzzy - uma fusão de redes neurais MLP e lógica fuzzy para aprimoramento do controle.

Este projeto visa comparar o desempenho de cada abordagem em relação à precisão de controle, adaptabilidade, eficiência e capacidade de lidar com incertezas.

## :file_folder: Estrutura do Projeto
   - **src/:** Código-fonte do projeto, organizado nas subpastas:
      - **FIS/:** Implementação do Sistema de Inferência Fuzzy.
      - **GeneticFuzzy/:** Implementação do Sistema Genético-Fuzzy.
      - **NeuroFuzzy/:** Implementação do Sistema Neuro-Fuzzy.

## :package: Pré-requisitos
ℹ️ Python 3.8 ou superior

## ⏯️ Uso
Cada sistema pode ser executado individualmente para testar o desempenho:

#### 1. Para o Sistema FIS:

```
python src/FIS/fuzzy_control.py
```

#### 2. Para o Sistema Genético-Fuzzy:

```
python src/GeneticFuzzy/genetic_fuzzy_control.py
```

#### 3. Para o Sistema Neuro-Fuzzy:

```
python src/NeuroFuzzy/neuro_fuzzy_control.py
```

##  :bar_chart: Comparação e Análise

Cada sistema será avaliado quanto a precisão, eficiência, adaptabilidade e robustez. Os resultados serão comparados quantitativamente e qualitativamente no relatório final.

## 👥 Membros da equipe

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/humberto-peres"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118866895?s=400&u=a12412e21705d58ab604be67c1e1431c80174b64&v=4" width="100px;" /><br /><sub><b>Humberto Peres da Rocha Filho</b></sub></a><br /><a href="https://github.com/humberto-peres" title="Humberto Peres da Rocha Filho"></a></td>
    <td align="center"><a href="https://github.com/Pellegr1n1"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/119978954?v=4" width="100px;"/><br /><sub><b>Leandro Pellegrini Fodi</b></sub></a><br /><a href="https://github.com/Pellegr1n1" title="Leandro Pellegrini Fodi"></a></td>
    <td align="center"><a href="https://github.com/v0cs"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104214178?v=4" width="100px;"/><br /><sub><b>Vítor Celestino</b></sub></a><br /><a href="https://github.com/v0cs" title="Vítor Celestino"></a></td>
    <td align="center"><a href="https://github.com/WesllyHn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/117309594?v=4" width="100px;"/><br /><sub><b>Weslly Hendler Neres</b></sub></a><br /><a href=https://github.com/WesllyHn" title="Weslly Hendler Neres"></a></td>
  </tr>
</table>
