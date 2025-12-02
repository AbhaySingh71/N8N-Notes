
  <h1>📘 n8n – Complete In-Depth Documentation</h1>
    

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

  
