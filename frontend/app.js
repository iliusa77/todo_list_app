var app = new Vue({
        el: '#tasks',

        data: {
            tasks: []
        },

        created: function () {
            this.fetchData();
        },

        methods: {
            fetchData: function () {
                this.$http.get('http://127.0.0.1:8000/tasks/')
                          .then(response => {
                             this.tasks = response.data
                             // or like this this.getTemp = response.json()
                          })
            }
        }

    })
    ;