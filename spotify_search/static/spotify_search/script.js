function App () {
  const self = this;

  const init = function () {
    // Default filter is by artist
    self.filterBy = "artist";

    $("#filter-dropdown li").on("click", function (e) {
      self.filterBy = $(e.currentTarget).data().value;
      $('#filter-by-button').html(self.filterBy.toUpperCase());
      self.search(self.getSearchKeyword(), self.filterBy);
    });

    $("#search-form").submit(function (e) {
      e.preventDefault();
      self.search(self.getSearchKeyword(), self.filterBy);
    });
  };

  this.getSearchKeyword = function () {
    return $("#formGroupInputLarge").val().replace(" ", "+");
  }

  this.search = function (keyword, filterBy) {
    if (!keyword && keyword.length === 0) return;

    this.changeUrlAndTitle(keyword, filterBy);
    $.ajax({
      url: "/search/",
      method: "POST",
      dataType: "json",
      beforeSend: function() {
        $("#results").html("");
        $('#loading-spinner').show();
      },
      data: {
        q: keyword,
        filter_by: filterBy,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
    }).done(function (data) {
      $('#loading-spinner').hide();
      $("#results").html(data.resultList);
      $("#result-count").html(data.count);
      $('#result-count-container').show();
      $('#result-type').html(self.filterBy + 's');
    }).error(function (err) {
      console.log(err);
    })
  };

  this.changeUrlAndTitle = function (keyword, filterBy) {
    window.history.pushState(
      {},
      filterBy + " named " + keyword,
      '/search/' + keyword + '/?' + $.param({filter_by: filterBy}),
    );
  };

  init();
}

$(document).ready(App);
