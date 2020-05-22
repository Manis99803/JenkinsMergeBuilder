node{
    // try {
        
    //     stage('Checkout') {
    //         git branch: 'test', url: 'git@github.com:Manis99803/JenkinsMergeBuilder.git'
    //     }
    //     stage('Test'){
    //         sh "python3 -m venv env"
    //         sh "source env/bin/activate"
    //         sh "pip3 install pytest"
    //         sh "pytest --cov=add  --junitxml=output.xml --cov-report=html test_file.py" 
    //         sh "ls"
    //     }
    //     stage('Publish Report'){
    //         publishHTML (target: [
    //             allowMissing: false,
    //             alwaysLinkToLastBuild: false,
    //             keepAll: true,
    //             reportDir: 'htmlcov',
    //             reportFiles: 'index.html',
    //             reportName: "RCov Report"
    //         ])
    //     }
    // } finally {
    //             junit 'output.xml'
    // }
    stage('Status')
    {
        sh 'commitId=$(git log --format="%H" -n 2 | tail -1)'
        sh 'echo ${commitId}'
        // sh 'printenv'
    }
}
