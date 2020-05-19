  
node {
    stage('Checkout') {
        checkout([$class: 'GitSCM', branches: [[name: "FETCH_HEAD"]],
                 extensions: [[$class: 'LocalBranch']],
                 userRemoteConfigs: [[refspec: "+refs/pull/*:refs/remotes/origin/pr/*", url: "git@github.com:Manis99803/JenkinsMergeBuilder.git"]]])
   }
}