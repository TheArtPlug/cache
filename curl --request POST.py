curl --request POST  

    --url https://api.cloudflare.com/client/v4/accounts/9e69505d9d471a2ce08ada8197454fbb/request-tracer/tracer     --header 'Content-Type: application/json'  

    --header 'Authorization: Bearer $CF_AUTH_TOKEN'  

    --data '{"url":"https://jubilant-telegram-6ppgvp4xjxph4jgg.github.dev/","method":"OPTIONS","headers":{"undefined":"undefined"},"cookies":{"undefined":"undefined"}}'curl -X POST https://gateway.ai.cloudflare.com/v1/9e69505d9d471a2ce08ada8197454fbb/theartplug/workers-ai/@cf/meta/llama-3.1-8b-instruct \
 --header 'Authorization: Bearer CF_TOKEN' \
 --header 'Content-Type: application/json' \
 --data '{"prompt": "What is Cloudflare?"}'