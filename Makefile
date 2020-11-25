NS = grzesrap
IMAGE = `basename $$PWD`

build:
	docker build $(CACHE_ARGS) -t $(IMAGE) .

push: build
	docker tag $(IMAGE) $(NS)/$(IMAGE)
	docker push $(NS)/$(IMAGE) 

redis-docker:
	docker-compose up -d redis

calc:
	docker-compose up calc

redis-k8s:
	kubectl create namespace calc
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm install redis bitnami/redis -n calc --set usePassword=false --set cluster.enabled=false

app-k8s:
	kubectl delete pod calc -n calc
	kubectl apply -f k8s/ -n calc