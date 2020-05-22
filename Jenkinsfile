node{
    try {
        stage('Checkout') {
        git branch: 'test', url: 'git@github.com:Manis99803/JenkinsMergeBuilder.git'
        }
        stage('Test'){
            sh "python3 -m venv env"
            sh "source env/bin/activate"
            sh "pip3 install pytest"
            sh "pytest --cov=add  --cov-report=xml test_file.py" 
            sh "ls"
        }
    } finally {
                junit 'build/reports/**/*.xml'
    }
}
