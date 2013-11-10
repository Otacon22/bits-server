/// <reference path="helpers/zepto.d.ts" />
/// <reference path="helpers/sockjs.d.ts" />
"use strict"

import v = require("view");
import c = require("controller");
import m = require("model");

$(function() {
    var controller = new c.Controller();
    v.IndexUI.create().init(controller);
});