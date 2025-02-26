from django.shortcuts import render
import os

def index(request):
    # 환경 변수 값 가져오기
    env_vars = {}
    secret_keys = ['SECRET_KEY', 'DB_PASSWORD', 'API_KEY']
    
    for key, value in os.environ.items():
        # 우리가 관심 있는 환경 변수만 표시
        if key in ['APP_NAME', 'DEBUG', 'HOST_URL', 'API_VERSION'] + secret_keys:
            # 민감한 정보는 마스킹 처리
            if key in secret_keys:
                value = value[:3] + '****' + value[-3:] if len(value) > 6 else '****'
            env_vars[key] = value

    return render(request, 'index.html', {
        'env_vars': env_vars,
        'secret_keys': secret_keys
    })
