var app = new Vue({
        el: '#tasks',

        data: {
            tasks: [],
            groups: []
        },

        created: function () {
            this.getTasksList();
            this.getGroupsList();
        },

        methods: {
            getTasksList: function () {
                this.$http.get('http://127.0.0.1:8000/tasks/')
                          .then(response => {
                             this.tasks = response.data
                             // or like this this.getTemp = response.json()
                          })
            },
            getGroupsList: function () {
                this.$http.get('http://127.0.0.1:8000/grouptasks/')
                          .then(response => {
                             this.groups = response.data
                             // or like this this.getTemp = response.json()
                          })
            }
        }

    })
    ;