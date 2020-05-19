  
node {
    stage('Pull Changes') {
        checkout scm
        // checkout([$class: 'GitSCM', branches: [[name: "FETCH_HEAD"]],
        //          extensions: [[$class: 'LocalBranch']],
        //          userRemoteConfigs: [[refspec: "+refs/pull/${ghprbPullId}:refs/remotes/origin/pr/${ghprbPullId}", url: "git@github.com:Manis99803/JenkinsMergeBuilder.git"]]])
   }
}