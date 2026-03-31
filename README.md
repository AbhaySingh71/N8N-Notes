<h1>📘 n8n – Complete In-Depth Documentation </h1>
    

   <section class="section">
          <h3>What is n8n?</h3>
          <p>n8n (<em>n-eight-n</em>) is a powerful workflow automation tool that connects different apps/services using a simple <strong>no-code + low-code</strong> approach.</p>
          <p><strong>Key Features</strong></p>
          <ul>
            <li>⚙️ 1200+ integrations</li>
            <li>🔄 Event-based + scheduled workflows</li>
            <li>💻 JavaScript support for custom logic</li>
            <li>🚀 Fully open-source + self-hosting</li>
            <li>🔐 Secure credentials storage</li>
          </ul>
        </section>

   <section class="section">
          <h2>🏗 1. n8n Core Concepts</h2>

  <h3>1.1 Workflows</h3>
          <p>A <strong>workflow</strong> is a series of connected nodes that automate a process. A workflow includes trigger nodes, action nodes, logic nodes and external integrations.</p>

   <h3>1.2 Nodes</h3>
          <p>Nodes are the building blocks of n8n.</p>
          <ul>
            <li><strong>Trigger Nodes</strong> — start a workflow (Webhook, Cron, Gmail, Notion)</li>
            <li><strong>Action Nodes</strong> — perform tasks (HTTP Request, OpenAI, Google Sheets, Airtable, MySQL)</li>
            <li><strong>Logic Nodes</strong> — add decision-making (IF, Switch, Merge, Split in Batches, Wait)</li>
            <li><strong>Function Nodes</strong> — custom JavaScript (Function, Function Item, Code, Set)</li>
          </ul>

   <h3>1.3 Data Flow</h3>
          <p>n8n passes data between nodes as JSON arrays of <code>items</code>:</p>
          <pre><code>{
  "items": [
    { "json": { "key": "value" } }
  ]
}</code></pre>
          <p>Access values with expressions like:</p>
          <pre><code>{{$json.field}}
{{$node["NodeName"].json["data"]}}
{{$env.MY_SECRET}}</code></pre>
        </section>

  <section class="section">
          <h2>🧰 2. Important Nodes Explained</h2>

   <h3>2.1 Webhook Node</h3>
          <p>Starts workflow from external calls (GET, POST, PUT, DELETE).</p>
          <p><strong>Use Cases</strong>: Receive data from apps, create custom APIs, connect forms → n8n.</p>

   <h3>2.2 Cron Node</h3>
          <p>Runs workflows automatically. Types: interval, daily/weekly, CRON expressions.</p>
        <h3>2.3 HTTP Request Node</h3>
     <p>Call any REST API. Supports JSON body, headers, query params, auth, file upload.</p>
          <h3>2.4 Function Node</h3>
          <p>Write JavaScript to manipulate data or run custom logic. Example:</p>
          <pre><code>return [
  {
    json: {
      fullName: `${$json.first} ${$json.last}`,
      age: $json.age + 1
    }
  }
];</code></pre>
          <h3>2.5 Merge Node</h3>
          <p>Combine branches of workflows. Modes: Append, Merge by key, Pass-through, Wait All.</p>
        </section>
        <section class="section">
          <h2>🔐 3. Credentials Management</h2>
          <p>n8n stores API keys & OAuth tokens securely.</p>
          <p><strong>Credential Types</strong>: API Key, OAuth2, Basic Auth, Custom Credentials.</p>
          <p><strong>Best Practices</strong>: do not hardcode keys, use environment variables, limit sharing.</p>
        </section>

   <section class="section">
          <h2>📊 4. Designing Workflows Like a Pro</h2>
          <h3>4.1 Naming Conventions</h3>
          <p>Use meaningful names such as <code>Fetch Orders API</code>, <code>Process User Data</code>, <code>Send Email Notification</code>.</p>

  <h3>4.2 Using Notes Node</h3>
          <p>Document purpose of branches, API details, expected inputs/outputs inside the workflow using Notes.</p>
     <h3>4.3 Error Handling</h3>
          <p>Use the <strong>Error Trigger Node</strong> to capture and route errors to Email, Slack, DB or monitoring systems.</p>
        </section>

   <section class="section">
          <h2>🧪 5. Testing & Debugging</h2>
          <h3>5.1 Manual Execution</h3>
          <p>Run workflows step-by-step for debugging.</p>

   <h3>5.2 Execution Logs</h3>
          <p>Examine node input/output, execution time and errors in the execution logs.</p>

   <h3>5.3 Debugging Tips</h3>
          <ul>
            <li>Use <em>Set</em> nodes to simplify data.</li>
            <li>Use <em>Function</em> nodes to log <code>$json</code>.</li>
            <li>Add No-Op or inspection nodes to probe data mid-flow.</li>
          </ul>
        </section>

   <section class="section">
          <h2>🚀 6. Deployment & Hosting</h2>
          <h3>6.1 Self-Hosting Methods</h3>
          <ul>
            <li><strong>Docker</strong> (recommended)</li>
            <li>Node.js</li>
            <li>Cloud: Render, Railway, DigitalOcean, AWS, GCP</li>
          </ul>
          <p><strong>Example env config:</strong></p>
          <pre><code>N8N_PORT=5678
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=password
WEBHOOK_TUNNEL_URL=https://your-url.ngrok.io</code></pre>
        </section>

  <section class="section">
          <h2>📦 7. Advanced Concepts</h2>
          <h3>7.1 Execution Modes</h3>
          <p>Regular Execution, Webhook Execution, Manual Debug Mode.</p>

  <h3>7.2 Sub-Workflows</h3>
          <p>Use <em>Execute Workflow</em> node to reuse logic across workflows. Example: main workflow sends lead → sub-workflow validates email.</p>

   <h3>7.3 Scaling & Concurrency</h3>
          <p>Use queue mode, Redis backend and multiple worker instances to handle high-traffic/bulk processing.</p>

   <h3>7.4 Using Databases</h3>
          <p>Supported DBs: PostgreSQL, MySQL, MongoDB, SQLite. Use them for logging, persisting workflow data, building custom APIs.</p>
        </section>

   <section class="section">
          <h2>🧾 8. Real-Life Use Cases</h2>
          <ul>
            <li><strong>E-commerce Automation</strong> — sync orders, update CRM, send notifications.</li>
            <li><strong>AI/LLM Automations</strong> — generate content, summaries, chatbot workflows.</li>
            <li><strong>CRM/Sheets Automations</strong> — sync contacts, update Notion CRM, auto-create tasks.</li>
            <li><strong>Custom APIs</strong> — Webhook + HTTP Request nodes to build API pipelines.</li>
          </ul>
        </section>

   <section class="section">
          <h2>🧹 9. Best Practices</h2>
          <ul>
            <li>Add Notes in every workflow</li>
            <li>Keep complex logic in sub-workflows</li>
            <li>Handle errors gracefully</li>
            <li>Use clear naming conventions</li>
            <li>Validate API responses</li>
            <li>Avoid overusing Function nodes for maintainability</li>
          </ul>
        </section>

   <section class="section">
          <h2>📚 10. Recommended Project Structure</h2>
          <pre><code>project-root/
├── workflows/
│   ├── user-management.json
│   ├── automation-daily.json
│
├── subworkflows/
│   ├── send-email.json
│   ├── validate-user.json
│
├── credentials/
│   ├── google.json
│   ├── mysql.json
│
└── docs/
    ├── API.md
    ├── endpoints.md</code></pre>

 </article>

  # 📘 n8n — Complete In-Depth


---

## What is n8n?

`n8n` (pronounced *n-eight-n*) is an extendable workflow automation tool for connecting APIs, databases, and services using a visual editor. It supports both **no-code** and **low-code** patterns by combining prebuilt integration nodes with JavaScript code nodes.

**Why use n8n?**

* Open source & self-hostable
* Flexible: use built-in integrations or HTTP requests to connect any REST API
* Programmable: Function/Code nodes allow advanced transformations
* Good for automation, ETL, lightweight integration services, webhooks, and prototypes

---

## Core Concepts

### Workflows

* A workflow is a directed graph of nodes. Each node performs a single responsibility (trigger, transform, API call, conditional, etc.).
* Workflows can be triggered by:

  * Webhooks (external calls)
  * Schedule/Cron
  * App-specific triggers (e.g., Gmail Trigger)
  * Manual execution for debugging
* Workflows can call other workflows via the **Execute Workflow** node (sub-workflows).

**Execution model**

* Each node receives `items`, an array of JSON objects with `json` (and optional `binary`) payloads:

```json
[
  {
    "json": { "id": 123, "name": "Alice" }
  }
]
```

* Each node processes input `items` and outputs new `items`. Nodes run sequentially along connected edges, with branching supported.

### Nodes (types)

* **Trigger nodes** — start workflows (Webhook, Cron, Gmail Trigger, etc.)
* **Action nodes** — interact with external services (HTTP Request, Google Sheets, Airtable, AWS, DB nodes)
* **Logic nodes** — IF, Switch, Merge, SplitInBatches, Wait, etc.
* **Function / Code nodes** — Function, Function Item, Code to run JS logic
* **Utility nodes** — Set, Rename Keys, Move Fields, NoOp
* **Credential nodes** — store API keys, OAuth tokens securely

### Expressions and how to use them

* Use `{{ }}` or the recommended `{{$json.field}}`, `{{$node["NodeName"].json["x"]}}` forms.
* Examples:

  * `{{$json.email}}`
  * `{{$node["HTTP Request"].json["status"]}}`
  * `{{$env.MY_SECRET}}`

**Tip:** Use the expression editor (gear icon) to build safe expressions; it shows real-time sample values.

---

## Important Nodes — Deep Dive

### 1) Webhook Node

**Purpose:** receive HTTP requests and start workflows.

**Key options:**

* HTTP method (GET/POST/PUT/DELETE)
* Response mode: `On Received` or `Last Node` (send response after workflow completes)
* Authentication & headers
* Path customization (unique URL path per workflow)

**Use cases:**

* Form submissions
* Payment gateway callbacks
* SaaS event callbacks (Stripe, GitHub, etc.)

**Best practices:**

* Use `Last Node` only when the workflow returns quickly; otherwise use `On Received` to return 200 quickly and process asynchronously.
* Validate incoming payloads early (Set/Function node) to prevent failures downstream.

---

### 2) Cron / Schedule Node

**Purpose:** schedule recurring flows.

**Options:** interval-based or CRON expression.

**Use cases:**

* Daily reports
* Periodic data sync
* Housekeeping tasks

**Best practices:**

* Use timezone-aware CRON expressions.
* Keep scheduled jobs idempotent (safe to run multiple times).

---

### 3) HTTP Request Node

**Purpose:** talk to any REST API.

**Key features:**

* Methods: GET/POST/PUT/PATCH/DELETE
* Auth: Basic/OAuth2/Api key/Custom headers
* Body types: JSON / Form-Data / Binary
* Pagination helpers (if built-in) or manual pagination using function nodes

**Respect rate limits**: implement retries with exponential backoff (Function + Wait nodes), or integrate with a queue to throttle.

**Example: calling an API**

```http
Method: POST
URL: https://api.example.com/v1/lead
Body (JSON): { "email": "{{$json.email}}", "name": "{{$json.name}}" }
```

---

### 4) Function & Code Nodes

**Purpose:** run JavaScript to transform items — powerful but makes workflows less visual.

**Types:**

* `Function` — receives all items and returns an array of transformed items.
* `Function Item` — transforms one item at a time.
* `Code` — a more advanced node supporting async/await and external libs depending on runtime.

**Example (Function Node):**

```js
return items.map(item => {
  const { firstName, lastName } = item.json;
  item.json.fullName = `${firstName} ${lastName}`.trim();
  return item;
});
```

**Best practices:**

* Keep JS small and focused — complex logic should be in sub-workflows or external services.
* Avoid storing secrets in code; use credentials or environment variables.

---

### 5) Merge, SplitInBatches, Wait, IF, Switch

**Merge** — combine two or more incoming streams. Modes: Append, Merge By Key, Pass-Through.

**SplitInBatches** — split a large array into batches to process sequentially (useful for rate-limited APIs).

**Wait** — delay execution (useful for polling, retries, or waiting for eventual consistency).

**IF / Switch** — conditional branching. Use `IF` for boolean checks; `Switch` for multi-way routing.

**Examples / Patterns:**

* Fan-out/Fan-in: Split dataset → parallel API calls (throttled) → Merge results.
* Poll until ready: Webhook triggers job creation → Wait + Poll loop until job done → Continue.

---

### 6) Credential nodes

* Credentials are stored in n8n's credential store and referenced by nodes.
* Support for OAuth2 flows: use the credentials UI to authorize apps like Google, GitHub.

**Security note:** Only users with proper roles should be able to edit credentials.

---

## Design Patterns & Best Practices

### Naming & Documentation

* Use clear node names: `Get Users (API)`, `Transform - Normalize Email`, `Send - Slack Notification`.
* Use `Note` nodes to explain the purpose, expected input/output, and edge cases.

### Modularity & Sub-workflows

* Extract repeatable logic into sub-workflows using `Execute Workflow`.
* Keep sub-workflows generic and parameterized via input items.

### Error Handling

* Use the global `Error Trigger` to catch unhandled errors and route them to logging/alerts.
* Within workflows, use `IF` checks and `Try/Catch` patterns (simulate with conditional branches) before calling fragile nodes.
* Implement retries with backoff using `Function` + `Wait` nodes or external queues.

**Example error flow:**

1. Node fails → n8n logs error
2. Error Trigger receives error → store to DB & send Slack alert
3. Optionally create a retry job in a queue

### Secrets & credentials

* Use credentials and environment variables for secrets.
* Do not commit exported workflows containing credentials. When exporting, n8n strips credential values.

### Versioning

* Use n8n's built-in workflow versioning (when available) or keep JSON exports under Git with clear change logs.
* Tag releases and include a `CHANGELOG.md` documenting workflow changes and API contract shifts.

---

## Data Handling & Transformation

### Typical data shapes

* **Simple item**: `{ json: { id: 1, name: 'Alice' } }`
* **Batch item**: array of items in a single payload — use `SplitInBatches` to iterate
* **Binary data**: files (images, PDFs) are stored in `binary` property; use `HTTP Request` with `binary` support or File nodes.

### Mapping techniques

* Prefer the `Set` node for simple mapping & renaming.
* Use `Function` nodes for complex maps or derived fields.
* Always document transformation expectations in the `Note` node.

### Pagination & rate limits

* If an API returns `next` links, use a loop pattern: `HTTP Request` → `Function` to check `next` → `SplitInBatches` or loop until `next` is null.
* Respect rate limits: implement throttling or process items in batches.

---

## Testing, Debugging & Observability

### Execution logs

* n8n UI provides per-node input/output and run metadata.
* Capture logs centrally (ELK, CloudWatch, Datadog) by forwarding error events.

### Manual testing

* Use `Manual` execution to run single nodes with sample inputs.
* Use temporary `Set` nodes to craft test payloads.

### Monitoring & metrics

* Monitor worker queue depth, failed executions, average execution time.
* Set up alerts on high failure rates or sudden execution spikes.

---

## Deployment & Scaling

### Self-hosting options

* **Docker (recommended)** — single container or Docker Compose with a DB (Postgres recommended)
* **Kubernetes** — recommended for larger scale: deploy n8n server + workers + Postgres + Redis (for queues)
* **Managed hosting** — n8n.cloud or PaaS platforms (Render, Railway)

### Production configuration (example env vars)

```
N8N_PORT=5678
N8N_HOST=0.0.0.0
N8N_PROTOCOL=http
N8N_EDITOR_BASE_URL=https://your.n8n.url
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=strongpassword
DB_TYPE=postgresdb
DB_POSTGRESDB_HOST=postgres
DB_POSTGRESDB_PORT=5432
DB_POSTGRESDB_DATABASE=n8n
DB_POSTGRESDB_USER=n8n
DB_POSTGRESDB_PASSWORD=securepassword
EXECUTIONS_PROCESS=main
EXECUTIONS_DATA_SAVE_ON_ERROR=all
EXECUTIONS_DATA_SAVE_ON_SUCCESS=none
QUEUE_BULL_REDIS_HOST=redis
QUEUE_BULL_REDIS_PORT=6379

# Webhook tunnel (if needed) for dev
WEBHOOK_TUNNEL_URL=https://your-ngrok-or-tunnel-url
```

**Notes:**

* Use Postgres in production instead of SQLite for reliability.
* Enable Basic Auth or OAuth for UI access.

### Scaling architecture

* **Single-instance** — small deployments, low throughput
* **Worker-based** — run one server + multiple worker containers to process executions in parallel
* **Kubernetes** with Horizontal Pod Autoscaler — scale workers and server as load increases

---

## Integrations & Real-world Use Cases

### E-commerce

* Order → Webhook → Process order → Update DB → Notify warehouse via Slack
* Sync inventory between Shopify and internal DB

### Marketing & CRM

* Capture leads from Typeform → Enrich via Clearbit → Create contact in HubSpot → Send welcome email

### AI/LLM

* Webhook receives user content → Call OpenAI via HTTP Request → Save summary to DB → Notify user

### Data pipelines

* Schedule ETL: pull data from REST → transform → push to data warehouse (BigQuery / Snowflake)

---

## Security Considerations

* Run n8n behind a proxy (NGINX) terminating TLS.
* Use strong Basic Auth or OAuth for the editor.
* Restrict who can edit credentials.
* Ensure exported workflow JSON does not include secrets.
* Harden DB and Redis with authentication & network rules.

---

## Project Structure & CI/CD

**Suggested repo layout**

```
repo-root/
├── workflows/               # exported JSON workflows
│   ├── automations/
│   │   ├── lead-processing.json
│   │   └── daily-sync.json
│   └── subworkflows/
├── infra/                   # k8s manifests / docker-compose
├── scripts/                 # helper scripts (deploy, migrate)
├── docs/
│   ├── RUNBOOK.md
│   └── API-Contracts.md
├── .github/workflows/       # CI for linting and deployment
└── README.md
```

**CI/CD tips**

* Validate JSON schema for exported workflows in CI.
* Run automated tests that call endpoints triggered by workflows.
* Deploy workflow changes to a staging n8n instance for manual verification prior to production.

---

## Appendices

### Example: Simple webhook → HTTP → DB workflow (JSON snippet)

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": { "httpMethod": "POST" }
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": { "url": "https://api.example.com/lead", "method": "POST", "body": {"name":"{{$json.name}}"}} 
    }
  ]
}
```

### Useful expressions & JS snippets

**Get current date ISO:**

```
{{ new Date().toISOString() }}
```

**Function node — map items to new shape:**

```js
return items.map(item => ({ json: { id: item.json.id, email: item.json.email.toLowerCase() } }));
```

**Retry with exponential backoff pseudo-pattern**

1. Track attempt count on item (`item.json._attempts`)
2. On failure, if attempts < max, `Wait` for `2 ** attempts * baseDelay` seconds and requeue

### Troubleshooting checklist

* Are credentials valid? Use a direct cURL call to verify.
* Is the webhook URL reachable from external service? Check firewall and proxy.
* Is Postgres/Redis reachable from n8n containers? Check network and authentication.
* Check node execution logs for input/output and errors.

---


