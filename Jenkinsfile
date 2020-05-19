node {
    stage('Checkout') {
        checkoutConfig.with {
        branches = [[ name: 'FETCH_HEAD' ]]
        userRemoteConfigs[0].refspec = '+refs/pull/*/head:refs/remotes/origin/pr/*'
        }
   }
}