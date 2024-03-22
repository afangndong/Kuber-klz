node {
    def app

    stage('Clone repository'){

        checkout scm
    }

    stage('Build image'){

        app = docker.build("afangndong/test-app-1")
    }

    stage('Test image'){

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image'){

        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('Trigger ManifestUpdate'){
        echo "Triggering updatemanifestjob"
        build job: 'Kuber-klz-Updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}