node{
    stage('Checkout') {
       git branch: 'test', url: 'git@github.com:Manis99803/JenkinsMergeBuilder.git'
   }
    stage('Test'){
        sh "python3 -m venv env"
        sh "source env/bin/activate"
        sh "pip3 install pytest"
        sh "pytest test_file.py" 
    }
    post {
        always {
            junit 'build/reports/**/*.xml'
        }
    }
}