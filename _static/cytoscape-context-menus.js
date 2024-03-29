! function(e, t) {
    "object" == typeof exports && "object" == typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define([], t) : "object" == typeof exports ? exports.cytoscapeContextMenus = t() : e.cytoscapeContextMenus = t()
}(self, (function() {
    return (() => {
        var e = {
                621: (e, t, n) => {
                    "use strict";

                    function i(e, t) {
                        (null == t || t > e.length) && (t = e.length);
                        for (var n = 0, i = new Array(t); n < t; n++) i[n] = e[n];
                        return i
                    }

                    function o(e) {
                        for (var t = "", n = 0; n < e.length; n++) t += e[n], n !== e.length - 1 && (t += " ");
                        return t
                    }

                    function r(e, t, n) {
                        n ? e.setAttribute(t, "") : e.removeAttribute(t)
                    }

                    function u(e, t, n) {
                        void 0 === customElements.get(e) && customElements.define(e, t, {
                            extends: n
                        })
                    }
                    n.r(t), n.d(t, {
                        contextMenus: () => O
                    });
                    var s = "cy-context-menus-divider",
                        a = {
                            evtType: "cxttap",
                            menuItems: [],
                            menuItemClasses: ["cy-context-menus-cxt-menuitem"],
                            contextMenuClasses: ["cy-context-menus-cxt-menu"],
                            submenuIndicator: {
                                src: "assets/submenu-indicator-default.svg",
                                width: 12,
                                height: 12
                            }
                        };

                    function c(e) {
                        return (c = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                            return typeof e
                        } : function(e) {
                            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                        })(e)
                    }

                    function l(e, t) {
                        var n;
                        if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                            if (Array.isArray(e) || (n = function(e, t) {
                                    if (e) {
                                        if ("string" == typeof e) return f(e, t);
                                        var n = Object.prototype.toString.call(e).slice(8, -1);
                                        return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? f(e, t) : void 0
                                    }
                                }(e)) || t && e && "number" == typeof e.length) {
                                n && (e = n);
                                var i = 0,
                                    o = function() {};
                                return {
                                    s: o,
                                    n: function() {
                                        return i >= e.length ? {
                                            done: !0
                                        } : {
                                            done: !1,
                                            value: e[i++]
                                        }
                                    },
                                    e: function(e) {
                                        throw e
                                    },
                                    f: o
                                }
                            }
                            throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                        }
                        var r, u = !0,
                            s = !1;
                        return {
                            s: function() {
                                n = e[Symbol.iterator]()
                            },
                            n: function() {
                                var e = n.next();
                                return u = e.done, e
                            },
                            e: function(e) {
                                s = !0, r = e
                            },
                            f: function() {
                                try {
                                    u || null == n.return || n.return()
                                } finally {
                                    if (s) throw r
                                }
                            }
                        }
                    }

                    function f(e, t) {
                        (null == t || t > e.length) && (t = e.length);
                        for (var n = 0, i = new Array(t); n < t; n++) i[n] = e[n];
                        return i
                    }

                    function d(e, t) {
                        if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
                    }

                    function h(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), Object.defineProperty(e, i.key, i)
                        }
                    }

                    function m(e, t, n) {
                        return t && h(e.prototype, t), n && h(e, n), e
                    }

                    function v(e, t) {
                        if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function");
                        e.prototype = Object.create(t && t.prototype, {
                            constructor: {
                                value: e,
                                writable: !0,
                                configurable: !0
                            }
                        }), t && C(e, t)
                    }

                    function y(e) {
                        var t = M();
                        return function() {
                            var n, i = I(e);
                            if (t) {
                                var o = I(this).constructor;
                                n = Reflect.construct(i, arguments, o)
                            } else n = i.apply(this, arguments);
                            return p(this, n)
                        }
                    }

                    function p(e, t) {
                        return !t || "object" !== c(t) && "function" != typeof t ? b(e) : t
                    }

                    function b(e) {
                        if (void 0 === e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                        return e
                    }

                    function g(e, t, n) {
                        return (g = "undefined" != typeof Reflect && Reflect.get ? Reflect.get : function(e, t, n) {
                            var i = function(e, t) {
                                for (; !Object.prototype.hasOwnProperty.call(e, t) && null !== (e = I(e)););
                                return e
                            }(e, t);
                            if (i) {
                                var o = Object.getOwnPropertyDescriptor(i, t);
                                return o.get ? o.get.call(n) : o.value
                            }
                        })(e, t, n || e)
                    }

                    function w(e) {
                        var t = "function" == typeof Map ? new Map : void 0;
                        return (w = function(e) {
                            if (null === e || (n = e, -1 === Function.toString.call(n).indexOf("[native code]"))) return e;
                            var n;
                            if ("function" != typeof e) throw new TypeError("Super expression must either be null or a function");
                            if (void 0 !== t) {
                                if (t.has(e)) return t.get(e);
                                t.set(e, i)
                            }

                            function i() {
                                return x(e, arguments, I(this).constructor)
                            }
                            return i.prototype = Object.create(e.prototype, {
                                constructor: {
                                    value: i,
                                    enumerable: !1,
                                    writable: !0,
                                    configurable: !0
                                }
                            }), C(i, e)
                        })(e)
                    }

                    function x(e, t, n) {
                        return (x = M() ? Reflect.construct : function(e, t, n) {
                            var i = [null];
                            i.push.apply(i, t);
                            var o = new(Function.bind.apply(e, i));
                            return n && C(o, n.prototype), o
                        }).apply(null, arguments)
                    }

                    function M() {
                        if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
                        if (Reflect.construct.sham) return !1;
                        if ("function" == typeof Proxy) return !0;
                        try {
                            return Date.prototype.toString.call(Reflect.construct(Date, [], (function() {}))), !0
                        } catch (e) {
                            return !1
                        }
                    }

                    function C(e, t) {
                        return (C = Object.setPrototypeOf || function(e, t) {
                            return e.__proto__ = t, e
                        })(e, t)
                    }

                    function I(e) {
                        return (I = Object.setPrototypeOf ? Object.getPrototypeOf : function(e) {
                            return e.__proto__ || Object.getPrototypeOf(e)
                        })(e)
                    }

                    function k(e) {
                        e.preventDefault(), e.stopPropagation()
                    }
                    var E = function(e) {
                            v(n, e);
                            var t = y(n);

                            function n(e, i, o) {
                                var u, s, a, c, l, f, h, m, v, y;
                                d(this, n), g((s = b(y = t.call(this)), I(n.prototype)), "setAttribute", s).call(s, "id", e.id);
                                var p = y._getMenuItemClassStr(o.cxtMenuItemClasses, e.hasTrailingDivider);
                                if (g((a = b(y), I(n.prototype)), "setAttribute", a).call(a, "class", p), g((c = b(y), I(n.prototype)), "setAttribute", c).call(c, "title", null !== (u = e.tooltipText) && void 0 !== u ? u : ""), e.disabled && r(b(y), "disabled", !0), e.image) {
                                    var w = document.createElement("img");
                                    w.src = e.image.src, w.width = e.image.width, w.height = e.image.height, w.style.position = "absolute", w.style.top = e.image.y + "px", w.style.left = e.image.x + "px", g((l = b(y), I(n.prototype)), "appendChild", l).call(l, w)
                                }
                                if (y.innerHTML += e.content, y.onMenuItemClick = i, y.data = {}, y.clickFns = [], y.selector = e.selector, y.hasTrailingDivider = e.hasTrailingDivider, y.show = void 0 === e.show || e.show, y.coreAsWell = e.coreAsWell || !1, y.scratchpad = o, void 0 === e.onClickFunction && void 0 === e.submenu) throw new Error("A menu item must either have click function or a submenu or both");
                                return y.onClickFunction = e.onClickFunction, e.submenu instanceof Array && y._createSubmenu(e.submenu), g((f = b(y), I(n.prototype)), "addEventListener", f).call(f, "mousedown", k), g((h = b(y), I(n.prototype)), "addEventListener", h).call(h, "mouseup", k), g((m = b(y), I(n.prototype)), "addEventListener", m).call(m, "touchstart", k), g((v = b(y), I(n.prototype)), "addEventListener", v).call(v, "touchend", k), y
                            }
                            return m(n, [{
                                key: "bindOnClickFunction",
                                value: function(e) {
                                    this.clickFns.push(e), g(I(n.prototype), "addEventListener", this).call(this, "click", e)
                                }
                            }, {
                                key: "unbindOnClickFunctions",
                                value: function() {
                                    var e, t = l(this.clickFns);
                                    try {
                                        for (t.s(); !(e = t.n()).done;) {
                                            var i = e.value;
                                            g(I(n.prototype), "removeEventListener", this).call(this, "click", i)
                                        }
                                    } catch (e) {
                                        t.e(e)
                                    } finally {
                                        t.f()
                                    }
                                    this.clickFns = []
                                }
                            }, {
                                key: "enable",
                                value: function() {
                                    r(this, "disabled", !1), this.hasSubmenu() && this.addEventListener("mouseenter", this.mouseEnterHandler)
                                }
                            }, {
                                key: "disable",
                                value: function() {
                                    r(this, "disabled", !0), this.hasSubmenu() && this.removeEventListener("mouseenter", this.mouseEnterHandler)
                                }
                            }, {
                                key: "hide",
                                value: function() {
                                    this.show = !1, this.style.display = "none"
                                }
                            }, {
                                key: "getHasTrailingDivider",
                                value: function() {
                                    return !!this.hasTrailingDivider
                                }
                            }, {
                                key: "setHasTrailingDivider",
                                value: function(e) {
                                    this.hasTrailingDivider = e
                                }
                            }, {
                                key: "hasSubmenu",
                                value: function() {
                                    return this.submenu instanceof S
                                }
                            }, {
                                key: "appendSubmenuItem",
                                value: function(e) {
                                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0;
                                    this.hasSubmenu() || this._createSubmenu(), this.submenu.appendMenuItem(e, t)
                                }
                            }, {
                                key: "isClickable",
                                value: function() {
                                    return void 0 !== this.onClickFunction
                                }
                            }, {
                                key: "display",
                                value: function() {
                                    this.show = !0, this.style.display = "block"
                                }
                            }, {
                                key: "isVisible",
                                value: function() {
                                    return !0 === this.show && "none" !== this.style.display
                                }
                            }, {
                                key: "removeSubmenu",
                                value: function() {
                                    this.hasSubmenu() && (this.submenu.removeAllMenuItems(), this.detachSubmenu())
                                }
                            }, {
                                key: "detachSubmenu",
                                value: function() {
                                    this.hasSubmenu() && (this.removeChild(this.submenu), this.removeChild(this.indicator), this.removeEventListener("mouseenter", this.mouseEnterHandler), this.removeEventListener("mouseleave", this.mouseLeaveHandler), this.submenu = void 0, this.indicator = void 0)
                                }
                            }, {
                                key: "_onMouseEnter",
                                value: function(e) {
                                    var t = this.getBoundingClientRect(),
                                        i = function(e) {
                                            e.style.opacity = "0", e.style.display = "block";
                                            var t = e.getBoundingClientRect();
                                            return e.style.opacity = "1", e.style.display = "none", t
                                        }(this.submenu),
                                        o = t.right + i.width > window.innerWidth,
                                        r = t.top + i.height > window.innerHeight;
                                    o || r ? o && !r ? (this.submenu.style.right = this.clientWidth + "px", this.submenu.style.top = "0px", this.submenu.style.left = "auto", this.submenu.style.bottom = "auto") : o && r ? (this.submenu.style.right = this.clientWidth + "px", this.submenu.style.bottom = "0px", this.submenu.style.top = "auto", this.submenu.style.left = "auto") : (this.submenu.style.left = this.clientWidth + "px", this.submenu.style.bottom = "0px", this.submenu.style.right = "auto", this.submenu.style.top = "auto") : (this.submenu.style.left = this.clientWidth + "px", this.submenu.style.top = "0px", this.submenu.style.right = "auto", this.submenu.style.bottom = "auto"), this.submenu.display();
                                    var u = Array.from(this.submenu.children).filter((function(e) {
                                            if (e instanceof n) return e.isVisible()
                                        })),
                                        a = u.length;
                                    u.forEach((function(e, t) {
                                        e instanceof n && (t < a - 1 && e.getHasTrailingDivider() ? e.classList.add(s) : e.getHasTrailingDivider() && e.classList.remove(s))
                                    }))
                                }
                            }, {
                                key: "_onMouseLeave",
                                value: function(e) {
                                    var t, n, i, o, r;
                                    t = {
                                        x: e.clientX,
                                        y: e.clientY
                                    }, n = this.submenu, o = t.y, (i = t.x) >= (r = n.getBoundingClientRect()).left && i <= r.right && o >= r.top && o <= r.bottom || this.submenu.hide()
                                }
                            }, {
                                key: "_createSubmenu",
                                value: function() {
                                    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : [];
                                    this.indicator = this.scratchpad.submenuIndicatorGen(), this.submenu = new S(this.onMenuItemClick, this.scratchpad), this.appendChild(this.indicator), this.appendChild(this.submenu);
                                    var t, i = l(e);
                                    try {
                                        for (i.s(); !(t = i.n()).done;) {
                                            var o = t.value,
                                                r = new n(o, this.onMenuItemClick, this.scratchpad);
                                            this.submenu.appendMenuItem(r)
                                        }
                                    } catch (e) {
                                        i.e(e)
                                    } finally {
                                        i.f()
                                    }
                                    this.mouseEnterHandler = this._onMouseEnter.bind(this), this.mouseLeaveHandler = this._onMouseLeave.bind(this), this.addEventListener("mouseenter", this.mouseEnterHandler), this.addEventListener("mouseleave", this.mouseLeaveHandler)
                                }
                            }, {
                                key: "_getMenuItemClassStr",
                                value: function(e, t) {
                                    return t ? e + " " + s : e
                                }
                            }], [{
                                key: "define",
                                value: function() {
                                    u("ctx-menu-item", n, "button")
                                }
                            }]), n
                        }(w(HTMLButtonElement)),
                        S = function(e) {
                            v(n, e);
                            var t = y(n);

                            function n(e, i) {
                                var o, r;
                                return d(this, n), g((o = b(r = t.call(this)), I(n.prototype)), "setAttribute", o).call(o, "class", i.cxtMenuClasses), r.style.position = "absolute", r.onMenuItemClick = e, r.scratchpad = i, r
                            }
                            return m(n, [{
                                key: "hide",
                                value: function() {
                                    this.isVisible() && (this.hideSubmenus(), this.style.display = "none")
                                }
                            }, {
                                key: "display",
                                value: function() {
                                    this.style.display = "block"
                                }
                            }, {
                                key: "isVisible",
                                value: function() {
                                    return "none" !== this.style.display
                                }
                            }, {
                                key: "hideMenuItems",
                                value: function() {
                                    var e, t = l(this.children);
                                    try {
                                        for (t.s(); !(e = t.n()).done;) {
                                            var n = e.value;
                                            n instanceof HTMLElement ? n.style.display = "none" : console.warn("".concat(n, " is not a HTMLElement"))
                                        }
                                    } catch (e) {
                                        t.e(e)
                                    } finally {
                                        t.f()
                                    }
                                }
                            }, {
                                key: "hideSubmenus",
                                value: function() {
                                    var e, t = l(this.children);
                                    try {
                                        for (t.s(); !(e = t.n()).done;) {
                                            var n = e.value;
                                            n instanceof E && n.submenu && n.submenu.hide()
                                        }
                                    } catch (e) {
                                        t.e(e)
                                    } finally {
                                        t.f()
                                    }
                                }
                            }, {
                                key: "appendMenuItem",
                                value: function(e) {
                                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0;
                                    if (void 0 !== t) {
                                        if (t.parentNode !== this) throw new Error("The item with id='".concat(t.id, "' is not a child of the context menu"));
                                        this.insertBefore(e, t)
                                    } else this.appendChild(e);
                                    e.isClickable() && this._performBindings(e)
                                }
                            }, {
                                key: "moveBefore",
                                value: function(e, t) {
                                    if (e.parentNode !== this) throw new Error("The item with id='".concat(e.id, "' is not a child of context menu"));
                                    if (t.parentNode !== this) throw new Error("The item with id='".concat(t.id, "' is not a child of context menu"));
                                    this.removeChild(e), this.insertBefore(e, t)
                                }
                            }, {
                                key: "removeAllMenuItems",
                                value: function() {
                                    for (; this.firstChild;) {
                                        var e = this.lastChild;
                                        e instanceof E ? this._removeImmediateMenuItem(e) : (console.warn("Found non menu item in the context menu: ", e), this.removeChild(e))
                                    }
                                }
                            }, {
                                key: "_removeImmediateMenuItem",
                                value: function(e) {
                                    if (!this._detachImmediateMenuItem(e)) throw new Error("menu item(id=".concat(e.id, ") is not in the context menu"));
                                    e.detachSubmenu(), e.unbindOnClickFunctions()
                                }
                            }, {
                                key: "_detachImmediateMenuItem",
                                value: function(e) {
                                    if (e.parentNode === this) {
                                        if (this.removeChild(e), this.children.length <= 0) {
                                            var t = this.parentNode;
                                            t instanceof E && t.detachSubmenu()
                                        }
                                        return !0
                                    }
                                    return !1
                                }
                            }, {
                                key: "_performBindings",
                                value: function(e) {
                                    var t = this._bindOnClick(e.onClickFunction);
                                    e.bindOnClickFunction(t), e.bindOnClickFunction(this.onMenuItemClick)
                                }
                            }, {
                                key: "_bindOnClick",
                                value: function(e) {
                                    var t = this;
                                    return function() {
                                        var n = t.scratchpad.currentCyEvent;
                                        e(n)
                                    }
                                }
                            }], [{
                                key: "define",
                                value: function() {
                                    u("menu-item-list", n, "div")
                                }
                            }]), n
                        }(w(HTMLDivElement)),
                        T = function(e) {
                            v(n, e);
                            var t = y(n);

                            function n(e, i) {
                                var o;
                                return d(this, n), (o = t.call(this, e, i)).onMenuItemClick = function(t) {
                                    k(t), o.hide(), e()
                                }, o
                            }
                            return m(n, [{
                                key: "removeMenuItem",
                                value: function(e) {
                                    var t = e.parentElement;
                                    t instanceof S && this.contains(t) && t._removeImmediateMenuItem(e)
                                }
                            }, {
                                key: "appendMenuItem",
                                value: function(e) {
                                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0;
                                    this.ensureDoesntContain(e.id), g(I(n.prototype), "appendMenuItem", this).call(this, e, t)
                                }
                            }, {
                                key: "insertMenuItem",
                                value: function(e) {
                                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
                                        n = t.before,
                                        i = t.parent;
                                    if (this.ensureDoesntContain(e.id), void 0 !== n) {
                                        if (!this.contains(n)) throw new Error("before(id=".concat(n.id, ") is not in the context menu"));
                                        var o = n.parentNode;
                                        if (!(o instanceof S)) throw new Error("Parent of before(id=".concat(n.id, ") is not a submenu"));
                                        o.appendMenuItem(e, n)
                                    } else if (void 0 !== i) {
                                        if (!this.contains(i)) throw new Error("parent(id=".concat(i.id, ") is not a descendant of the context menu"));
                                        i.appendSubmenuItem(e)
                                    } else this.appendMenuItem(e)
                                }
                            }, {
                                key: "moveBefore",
                                value: function(e, t) {
                                    var n = e.parentElement;
                                    if (!this.contains(n)) throw new Error("parent(id=".concat(n.id, ") is not in the contex menu"));
                                    if (!this.contains(t)) throw new Error("before(id=".concat(t.id, ") is not in the context menu"));
                                    n.removeChild(e), this.insertMenuItem(e, {
                                        before: t
                                    })
                                }
                            }, {
                                key: "moveToSubmenu",
                                value: function(e) {
                                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null,
                                        n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : null,
                                        i = e.parentElement;
                                    if (!(i instanceof S)) throw new Error("current parent(id=".concat(i.id, ") is not a submenu"));
                                    if (!this.contains(i)) throw new Error("parent of the menu item(id=".concat(i.id, ") is not in the context menu"));
                                    if (null !== t) {
                                        if (!this.contains(t)) throw new Error("parent(id=".concat(t.id, ") is not in the context menu"));
                                        i._detachImmediateMenuItem(e), t.appendSubmenuItem(e)
                                    } else null !== n && (e.selector = n.selector, e.coreAsWell = n.coreAsWell), i._detachImmediateMenuItem(e), this.appendMenuItem(e)
                                }
                            }, {
                                key: "ensureDoesntContain",
                                value: function(e) {
                                    var t = document.getElementById(e);
                                    if (void 0 !== t && this.contains(t)) throw new Error("There is already an element with id=".concat(e, " in the context menu"))
                                }
                            }], [{
                                key: "define",
                                value: function() {
                                    u("ctx-menu", n, "div")
                                }
                            }]), n
                        }(S);

                    function A(e, t) {
                        (null == t || t > e.length) && (t = e.length);
                        for (var n = 0, i = new Array(t); n < t; n++) i[n] = e[n];
                        return i
                    }

                    function O(e) {
                        var t = this;
                        t.scratch("cycontextmenus") || t.scratch("cycontextmenus", {});
                        var n, r, u = function(e) {
                                return t.scratch("cycontextmenus")[e]
                            },
                            c = function(e, n) {
                                return t.scratch("cycontextmenus")[e] = n
                            },
                            l = u("options"),
                            f = u("cxtMenu"),
                            d = function(e) {
                                var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0,
                                    n = m(e);
                                if (void 0 !== t) {
                                    var i = y(t);
                                    f.insertMenuItem(n, {
                                        parent: i
                                    })
                                } else f.insertMenuItem(n)
                            },
                            h = function(e) {
                                for (var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0, n = 0; n < e.length; n++) d(e[n], t)
                            },
                            m = function(e) {
                                var n = t.scratch("cycontextmenus");
                                return new E(e, f.onMenuItemClick, n)
                            },
                            v = function() {
                                u("active") && (f.removeAllMenuItems(), t.off("tapstart", u("eventCyTapStart")), t.off(l.evtType, u("onCxttap")), t.off("viewport", u("onViewport")), document.removeEventListener("mouseup", u("hideOnNonCyClick")), f.parentNode.removeChild(f), f = void 0, c("cxtMenu", void 0), c("active", !1), c("anyVisibleChild", !1), c("onCxttap", void 0), c("onViewport", void 0), c("hideOnNonCyClick", void 0))
                            },
                            y = function(e) {
                                var t = document.getElementById(e);
                                if (t instanceof E) return t;
                                throw new Error("The item with id=".concat(e, " is not a menu item"))
                            };
                        if ("get" !== e) {
                            E.define(), S.define(), T.define(), l = function(e, t) {
                                var n = {};
                                for (var i in e) n[i] = e[i];
                                for (var o in t) n[o] instanceof Array ? n[o] = n[o].concat(t[o]) : n[o] = t[o];
                                return n
                            }(a, e), c("options", l), u("active") && v(), c("active", !0), c("submenuIndicatorGen", function(e) {
                                var t = document.createElement("img");
                                return t.src = e.src, t.width = e.width, t.height = e.height, t.classList.add("cy-context-menus-submenu-indicator"), t
                            }.bind(void 0, l.submenuIndicator));
                            var p = o(l.contextMenuClasses);
                            c("cxtMenuClasses", p);
                            var b = t.scratch("cycontextmenus");
                            f = new T((function() {
                                return c("cxtMenuPosition", void 0)
                            }), b), c("cxtMenu", f), t.container().appendChild(f), c("cxtMenuItemClasses", o(l.menuItemClasses));
                            var g = l.menuItems;
                            h(g), r = function(e) {
                                    c("currentCyEvent", e),
                                        function(e) {
                                            var n, i = t.container(),
                                                o = u("cxtMenuPosition"),
                                                r = e.position || e.cyPosition;
                                            if (o != r) {
                                                f.hideMenuItems(), c("anyVisibleChild", !1), c("cxtMenuPosition", r);
                                                var s = {
                                                        top: (n = i.getBoundingClientRect()).top,
                                                        left: n.left
                                                    },
                                                    a = e.renderedPosition || e.cyRenderedPosition,
                                                    l = getComputedStyle(i)["border-width"],
                                                    d = parseInt(l.replace("px", "")) || 0;
                                                d > 0 && (s.top += d, s.left += d);
                                                var h = i.clientHeight,
                                                    m = i.clientWidth,
                                                    v = h / 2,
                                                    y = m / 2;
                                                a.y > v && a.x <= y ? (f.style.left = a.x + "px", f.style.bottom = h - a.y + "px", f.style.right = "auto", f.style.top = "auto") : a.y > v && a.x > y ? (f.style.right = m - a.x + "px", f.style.bottom = h - a.y + "px", f.style.left = "auto", f.style.top = "auto") : a.y <= v && a.x <= y ? (f.style.left = a.x + "px", f.style.top = a.y + "px", f.style.right = "auto", f.style.bottom = "auto") : (f.style.right = m - a.x + "px", f.style.top = a.y + "px", f.style.left = "auto", f.style.bottom = "auto")
                                            }
                                        }(e);
                                    var n, i = e.target || e.cyTarget,
                                        o = function(e, t) {
                                            var n;
                                            if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                                                if (Array.isArray(e) || (n = function(e, t) {
                                                        if (e) {
                                                            if ("string" == typeof e) return A(e, t);
                                                            var n = Object.prototype.toString.call(e).slice(8, -1);
                                                            return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? A(e, t) : void 0
                                                        }
                                                    }(e)) || t && e && "number" == typeof e.length) {
                                                    n && (e = n);
                                                    var i = 0,
                                                        o = function() {};
                                                    return {
                                                        s: o,
                                                        n: function() {
                                                            return i >= e.length ? {
                                                                done: !0
                                                            } : {
                                                                done: !1,
                                                                value: e[i++]
                                                            }
                                                        },
                                                        e: function(e) {
                                                            throw e
                                                        },
                                                        f: o
                                                    }
                                                }
                                                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                                            }
                                            var r, u = !0,
                                                s = !1;
                                            return {
                                                s: function() {
                                                    n = e[Symbol.iterator]()
                                                },
                                                n: function() {
                                                    var e = n.next();
                                                    return u = e.done, e
                                                },
                                                e: function(e) {
                                                    s = !0, r = e
                                                },
                                                f: function() {
                                                    try {
                                                        u || null == n.return || n.return()
                                                    } finally {
                                                        if (s) throw r
                                                    }
                                                }
                                            }
                                        }(f.children);
                                    try {
                                        for (o.s(); !(n = o.n()).done;) {
                                            var r = n.value;
                                            r instanceof E && (i === t ? r.coreAsWell : i.is(r.selector)) && r.show && (f.display(), c("anyVisibleChild", !0), r.display())
                                        }
                                    } catch (e) {
                                        o.e(e)
                                    } finally {
                                        o.f()
                                    }
                                    var a = Array.from(f.children).filter((function(e) {
                                            if (e instanceof E) return e.isVisible()
                                        })),
                                        l = a.length;
                                    a.forEach((function(e, t) {
                                        e instanceof E && (t < l - 1 && e.getHasTrailingDivider() ? e.classList.add(s) : e.getHasTrailingDivider() && e.classList.remove(s))
                                    })), !u("anyVisibleChild") && ! function(e) {
                                        return e.offsetWidth <= 0 && e.offsetHeight <= 0 || e.style && e.style.display || getComputedStyle(e).display
                                    }(f) && f.hide()
                                }, t.on(l.evtType, r), c("onCxttap", r),
                                function() {
                                    var e = function(e) {
                                        if (f.contains(e.originalEvent.target)) return !1;
                                        f.hide(), c("cxtMenuPosition", void 0), c("currentCyEvent", void 0)
                                    };
                                    t.on("tapstart", e), c("eventCyTapStart", e);
                                    var n = function() {
                                        f.hide()
                                    };
                                    t.on("viewport", n), c("onViewport", n)
                                }(), n = function(e) {
                                    t.container().contains(e.target) || f.contains(e.target) || (f.hide(), c("cxtMenuPosition", void 0))
                                }, document.addEventListener("mouseup", n), c("hideOnNonCyClick", n),
                                function() {
                                    var e, t = function(e, t) {
                                        var n;
                                        if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                                            if (Array.isArray(e) || (n = function(e, t) {
                                                    if (e) {
                                                        if ("string" == typeof e) return i(e, t);
                                                        var n = Object.prototype.toString.call(e).slice(8, -1);
                                                        return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? i(e, t) : void 0
                                                    }
                                                }(e)) || t && e && "number" == typeof e.length) {
                                                n && (e = n);
                                                var o = 0,
                                                    r = function() {};
                                                return {
                                                    s: r,
                                                    n: function() {
                                                        return o >= e.length ? {
                                                            done: !0
                                                        } : {
                                                            done: !1,
                                                            value: e[o++]
                                                        }
                                                    },
                                                    e: function(e) {
                                                        throw e
                                                    },
                                                    f: r
                                                }
                                            }
                                            throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                                        }
                                        var u, s = !0,
                                            a = !1;
                                        return {
                                            s: function() {
                                                n = e[Symbol.iterator]()
                                            },
                                            n: function() {
                                                var e = n.next();
                                                return s = e.done, e
                                            },
                                            e: function(e) {
                                                a = !0, u = e
                                            },
                                            f: function() {
                                                try {
                                                    s || null == n.return || n.return()
                                                } finally {
                                                    if (a) throw u
                                                }
                                            }
                                        }
                                    }(document.getElementsByClassName("cy-context-menus-cxt-menu"));
                                    try {
                                        for (t.s(); !(e = t.n()).done;) e.value.addEventListener("contextmenu", (function(e) {
                                            return e.preventDefault()
                                        }))
                                    } catch (e) {
                                        t.e(e)
                                    } finally {
                                        t.f()
                                    }
                                }()
                        }
                        return function(e) {
                            return {
                                isActive: function() {
                                    return u("active")
                                },
                                appendMenuItem: function(t) {
                                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0;
                                    return d(t, n), e
                                },
                                appendMenuItems: function(t) {
                                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : void 0;
                                    return h(t, n), e
                                },
                                removeMenuItem: function(t) {
                                    var n = y(t);
                                    return f.removeMenuItem(n), e
                                },
                                setTrailingDivider: function(t, n) {
                                    var i = y(t);
                                    return i.setHasTrailingDivider(n), n ? i.classList.add(s) : i.classList.remove(s), e
                                },
                                insertBeforeMenuItem: function(t, n) {
                                    var i = m(t),
                                        o = y(n);
                                    return f.insertMenuItem(i, {
                                        before: o
                                    }), e
                                },
                                moveToSubmenu: function(t) {
                                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null,
                                        i = y(t);
                                    if (null === n) f.moveToSubmenu(i);
                                    else if ("string" == typeof n) {
                                        var o = y(n.toString());
                                        f.moveToSubmenu(i, o)
                                    } else void 0 !== n.coreAsWell || void 0 !== n.selector ? f.moveToSubmenu(i, null, n) : console.warn("options neither has coreAsWell nor selector property but it is an object. Are you sure that this is what you want to do?");
                                    return e
                                },
                                moveBeforeOtherMenuItem: function(t, n) {
                                    var i = y(t),
                                        o = y(n);
                                    return f.moveBefore(i, o), e
                                },
                                disableMenuItem: function(t) {
                                    return y(t).disable(), e
                                },
                                enableMenuItem: function(t) {
                                    return y(t).enable(), e
                                },
                                hideMenuItem: function(t) {
                                    return y(t).hide(), e
                                },
                                showMenuItem: function(t) {
                                    return y(t).display(), e
                                },
                                destroy: function() {
                                    return v(), e
                                }
                            }
                        }(this)
                    }
                },
                579: (e, t, n) => {
                    var i = n(621).contextMenus,
                        o = function(e) {
                            e && e("core", "contextMenus", i)
                        };
                    "undefined" != typeof cytoscape && o(cytoscape), e.exports = o
                }
            },
            t = {};

        function n(i) {
            var o = t[i];
            if (void 0 !== o) return o.exports;
            var r = t[i] = {
                exports: {}
            };
            return e[i](r, r.exports, n), r.exports
        }
        return n.d = (e, t) => {
            for (var i in t) n.o(t, i) && !n.o(e, i) && Object.defineProperty(e, i, {
                enumerable: !0,
                get: t[i]
            })
        }, n.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t), n.r = e => {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }), Object.defineProperty(e, "__esModule", {
                value: !0
            })
        }, n(579)
    })()
}));