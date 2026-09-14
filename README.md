<img src="https://raw.githubusercontent.com/mysterious-joker/mysterious-joker/main/assets/profile-header.png?v=1" alt="Lim Zi Chao — AI, Software and Data Engineering. NUS Computer Science and Mathematics. ASEAN Undergraduate Scholar." width="100%" />

<p align="center">
  <a href="#selected-system"><strong>Selected system</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#experience"><strong>Experience</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#toolkit"><strong>Toolkit</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/lzc-nus"><strong>NUS work ↗</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/limzichao/"><strong>LinkedIn ↗</strong></a>
</p>

I'm **Lim Zi Chao**, an NUS Computer Science undergraduate pursuing a second major in Mathematics, an **ASEAN Undergraduate Scholar**, and a **Data Engineer Intern at Theme International Trading**.

<p>
  <a href="https://www.linkedin.com/in/limzichao/">Connect on LinkedIn</a>
</p>

<a id="selected-system"></a>

## Selected Project

### [Shopping Copilot — TikTok TechJam 2026](https://github.com/i-anything/TTSC)

**Team lead · 5th place · Presented at TikTok Singapore**

I led a five-person team and owned the hybrid retrieval architecture for a deterministic, CPU-only conversational search agent over 50,000 products. It asks focused questions, fuses lexical and semantic evidence, and returns ranked recommendations without runtime network access or paid APIs.

<details>
<summary><strong>Open the engineering case study</strong></summary>

#### What I owned

- Designed and implemented the retrieval architecture: BM25, dense embeddings, reciprocal-rank fusion, route gating, and exact structured-evidence reranking.
- Coordinated retrieval, dialogue, evaluation, and preprocessing across the five-person team.
- Presented the final system at TikTok Singapore.

#### Public evaluation

| Metric | Result | Context |
| :--- | ---: | :--- |
| Hit Rate@10 | **1.000** | 200 official public-evaluation sessions |
| MRR | **1.000** | 200 official public-evaluation sessions |
| TechnicalScore | **0.9805** | Official public evaluator |
| Response latency | **44.43 ms p95** | Measured development machine |

These are public development-set results. Hardware, workload, and evaluation distribution affect performance.

#### Why the design matters

The system is deterministic and fail-open: every session is reproducible, and lexical retrieval remains available when dense assets cannot initialize. Runtime cost is **USD 0** because reset and response paths make no hosted-model or external API calls.

[Read the source and technical documentation →](https://github.com/i-anything/TTSC)

</details>

<br>

## Selected NUS Projects

My coursework and school projects live on **[@lzc-nus](https://github.com/lzc-nus)**, while this account stays focused on personal and professional work.

<table width="100%" cellpadding="16" cellspacing="0">
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/lzc-nus/Plutus">Plutus ↗</a></h3>
      <p><strong>NUS Orbital · Deployed full-stack platform</strong></p>
      <p>A financial platform with protected user-data APIs, validated transaction workflows, and typed frontend/backend contracts.</p>
      <p><code>Next.js</code> <code>TypeScript</code> <code>FastAPI</code> <code>PostgreSQL</code> <code>Docker</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/lzc-nus/ip">Green Chonk ↗</a></h3>
      <p><strong>NUS Software Engineering · JavaFX</strong></p>
      <p>A persistent task companion with date-aware scheduling, resilient command parsing, a CLI fallback, and regression tests.</p>
      <p><code>Java</code> <code>JavaFX</code> <code>Gradle</code> <code>JUnit</code></p>
    </td>
  </tr>
</table>

<a id="experience"></a>

## Experience

<details>
<summary><strong>What I build as a data engineer intern at quantitative trading firm</strong></summary>

- Engineer Python and SQL infrastructure connecting market information and governed PostgreSQL datasets to analyst and AI-agent workflows.
- Architected a source-to-canonical commodity-data pipeline spanning API and blob ingestion, transformation, staging, validation, lineage, replayability, and controlled publication.
- Built vendor API ingestion workflows and backfilled missing market data into Azure-hosted PostgreSQL.
- Prototyped semantic chunking, embeddings, vector retrieval, RAG, persistent agent memory, and MCP tool interfaces for governed knowledge sources.

</details>

<details>
<summary><strong>Academic foundation and earlier experience</strong></summary>

**National University of Singapore** · B.Comp. Computer Science, Second Major in Mathematics  
2025–December 2028 expected · ASEAN Undergraduate Scholarship

Relevant coursework: Data Structures & Algorithms, Software Engineering, Database Systems, Computer Organization, Introduction to Data Science, Probability, Linear Algebra, and Calculus.

**Student Associate, NUS Libraries** · December 2025–January 2026  
Automated batch document processing and output validation with PowerShell, improving naming, organization, and record consistency.

**Languages:** English and Chinese (native/bilingual); Malay (conversational).

</details>

<a id="toolkit"></a>

## Toolkit

<details>
<summary><strong>Complete technical inventory</strong></summary>

| Focus | Tools & methods |
| :--- | :--- |
| Programming | Python, SQL, Java, C++, TypeScript / JavaScript |
| Search & ML | Pandas, NumPy, BM25, dense embeddings, vector search, reciprocal-rank fusion, ranking and reranking, ONNX Runtime, evaluation metrics |
| AI systems | AI agents, MCP, RAG, semantic chunking, persistent memory |
| Data engineering | ETL / ELT, API ingestion, preprocessing, validation, lineage, replayability, PostgreSQL, Azure |
| Application engineering | FastAPI, REST APIs, React / Next.js, Docker, Git, testing and debugging |

</details>

<p align="center">
  <a href="mailto:zichao2006@gmail.com"><strong>Email me</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/limzichao/"><strong>LinkedIn</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/lzc-nus"><strong>NUS GitHub</strong></a>
</p>
