node {
    stage('Checkout') {
        sh "echo ${env.BRANCH_NAME}"
        checkoutConfig.with {
        branches = [[ name: 'FETCH_HEAD' ]]
        userRemoteConfigs[0].refspec = '+refs/pull/*/head:refs/remotes/origin/pr/*'
        }
   }
}