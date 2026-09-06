<div align="center">
  <img src="https://subreddit-scrape-presentjay.koyeb.app/" width="400" title="Meme" alt="Refresh the page for another one." />
</div>

---

### Hyeonjae Jeong

Data platform engineer at AB180. Feature platform and inference serving for an ad product. dbt/Snowflake on the training side, Python and Go services on the serving side.

**Where I've been**

- **AB180** · 2023.04 – now — data platform (dbt, Snowflake, Airflow) and the ML feature platform. Reporting backend before that, and a stint doing data business development on the side.
- **ETRI** · 2021.03 – 2023.02 — integrated authn/authz for an open data hub. Keycloak, Kafka, Debezium CDC. Two first-author KCI papers and an M.S. from UST came out of it.

**What I do well**

- Finding defects nobody reported. Chronic undercounts in customer-facing numbers, a warehouse burning credits with no query behind it, a training pipeline that referenced its own downstream report.
- Turning the fix into a check, so the same thing can't come back. Both projects below started that way.
- Counting the cost before building. I've cancelled my own designs on that basis.

**Making**

- **[dbt-plan](https://github.com/PresentJay/dbt-plan)** [![pypi](https://img.shields.io/pypi/v/dbt-plan)](https://pypi.org/project/dbt-plan/) [![forks](https://img.shields.io/github/forks/PresentJay/dbt-plan?style=flat)](https://github.com/PresentJay/dbt-plan/forks) [![last commit](https://img.shields.io/github/last-commit/PresentJay/dbt-plan)](https://github.com/PresentJay/dbt-plan/commits) — `terraform plan`, for dbt. Warns about destructive DDL and broken downstream refs before `dbt run`. Static analysis of compiled SQL, no warehouse connection. `pip install dbt-plan` · listed in [awesome-dbt](https://github.com/Hiflylabs/awesome-dbt)
- **[zero-shelter](https://github.com/zero-shelter/zero-shelter)** — turns scanner output into a short list of what to fix now. TypeScript, no LLM at runtime.
- **[autopilot-skills](https://github.com/PresentJay/autopilot-skills)** — mission runner for AI coding agents. Risk-tiered diff limits and a pre-execute deny list.
- **[lightweight-kubernetes-sandbox-cli](https://github.com/PresentJay/lightweight-kubernetes-sandbox-cli)** — k3s cluster setup and ops CLI, from the ETRI years.

presentj94@gmail.com
