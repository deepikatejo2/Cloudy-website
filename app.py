from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')
  # return "<p>This is the home page</p>"

@app.route("/services")
def services():
  cloud_services = [
      {
          "name": "Cloud Compute Engine",
          "category": "Compute",
          "price": "$10 / mo",
          "desc": "Scalable Linux and Windows virtual machines equipped with high-frequency CPU cores. Designed for web application hosting, microservices, and rapid deployment environments with full root access.",
          "badge": "Popular"
      },
      {
          "name": "High-Memory Instances",
          "category": "Compute",
          "price": "$42 / mo",
          "desc": "Dedicated RAM-optimized virtual servers tailored for memory-heavy operations, real-time data analytics, enterprise software, and in-memory caching solutions like Redis and Memcached.",
          "badge": "Enterprise"
      },
      {
          "name": "NVMe Block Storage",
          "category": "Storage",
          "price": "$0.10 / GB",
          "desc": "Ultra-low latency SSD block storage volumes that attach seamlessly to your compute instances. Features automated encryption at rest, on-the-fly resizing, and snapshot capability for high-I/O workloads.",
          "badge": "Fast I/O"
      },
      {
          "name": "S3-Compatible Object Storage",
          "category": "Storage",
          "price": "$0.02 / GB",
          "desc": "Highly available and durable cloud storage engineered for unstructured files, media libraries, static website hosting, and database backups. Fully compatible with AWS S3 APIs and tools.",
          "badge": "Scalable"
      },
      {
          "name": "Managed PostgreSQL Database",
          "category": "Database",
          "price": "$25 / mo",
          "desc": "Production-ready relational database instances handled entirely by our team. Includes automated software patching, daily encrypted backups, continuous point-in-time recovery, and auto-failover high availability.",
          "badge": "Managed"
      },
      {
          "name": "Managed Redis Cache",
          "category": "Database",
          "price": "$18 / mo",
          "desc": "Fully managed, blazingly fast in-memory key-value data stores. Optimize application response times by offloading repetitive database queries, managing user session states, and processing pub/sub messaging.",
          "badge": "Performance"
      },
      {
          "name": "Global Load Balancer",
          "category": "Networking",
          "price": "$15 / mo",
          "desc": "Intelligent HTTP/HTTPS and TCP traffic distribution across multiple compute nodes. Automatically detects unhealthy instances, performs seamless failovers, and offers built-in DDoS protection and free SSL management.",
          "badge": "Security"
      },
      {
          "name": "Kubernetes Engine (CKE)",
          "category": "Containers",
          "price": "$30 / mo",
          "desc": "Automate the deployment, scaling, and management of containerized applications. Features a fully managed control plane with automated cluster health monitoring and one-click node pool expansion.",
          "badge": "DevOps"
      }
    ]
  return render_template('services.html', services=cloud_services)

CLOUD_SERVICES = [
    "Cloud Compute Engine ($10 / mo)",
    "High-Memory Instances ($42 / mo)",
    "NVMe Block Storage ($0.10 / GB)",
    "S3-Compatible Object Storage ($0.02 / GB)",
    "Managed PostgreSQL Database ($25 / mo)",
    "Managed Redis Cache ($18 / mo)",
    "Global Load Balancer ($15 / mo)",
    "Kubernetes Engine (CKE) ($30 / mo)"
]

@app.route("/order", methods=['GET','POST'])
def order():
  if request.method == 'POST':
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    selected_service = request.form.get('selected_service')
    instances = request.form.get('instances')
    region = request.form.get('region')
    return render_template(
      'order.html',
      services=CLOUD_SERVICES,
      success=True,
      order_details={
        'name': user_name,
        'email': user_email,
        'selected_service': selected_service,
        'instances': instances,
        'region': region
        }
      )
  return render_template('order.html', services=CLOUD_SERVICES,success=False)    

if __name__ == "__main__":
  app.run(debug=True, port=8000)  